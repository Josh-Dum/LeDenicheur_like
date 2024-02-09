import scrapy
import pymongo
from scrapy.utils.project import get_project_settings
import urllib.parse
from scrapy_app.items import IphoneItem 
from datetime import datetime
import pymongo
import os
import re
import json

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.fr']
    # start_urls = ['https://www.amazon.fr/s?k=iphone15+pro+1To+titane+naturel']



    produits ={}

    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)

        # Connexion à MongoDB
        mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client['iphone_db']
        self.models = self.db['models']

        # Ajouter un log pour confirmer la connexion
        self.logger.info("Connexion à MongoDB réussie")
        self.logger.info(f"Base de données: {self.db.name}, Collection: {self.models.name}")
        # Charger les données existantes
        self.charger_donnees_existantes()


    def charger_donnees_existantes(self):
        try:
            with open('/app/data_json/donnees_produits.json', 'r', encoding='utf-8') as f:
                self.produits = json.load(f)
        except FileNotFoundError:
            self.produits = {}



    def start_requests(self):
        
        # Récupération des informations de MongoDB pour construire les URLs
        for model in self.db.models.find({}):
            gamme = model["gamme"]
            for modele in model["modèles"]:
                nom_modele = modele["nom"]
                for variante in modele["variantes"]:
                    stockage = variante["stockage"]
                    for couleur in variante["couleurs"]:
                        couleur_nom = couleur["couleur"]

                        query = f"{nom_modele} {stockage} {couleur_nom}".replace(" ", "+")
                        url = f"https://www.amazon.fr/s?k={urllib.parse.quote(query)}"

                        # Création de l'objet meta pour passer les informations supplémentaires
                        meta_info = {
                            'gamme': gamme,
                            'nom': nom_modele,
                            'stockage': stockage,
                            'couleur': couleur_nom
                        }
                        yield scrapy.Request(url, self.parse, meta={'model_info': meta_info})



    
    def parse(self, response):

        # Extraire les informations de l'URL pour comparaison
        url_info = response.meta.get('model_info', {})
        url_model = url_info.get('nom')
        url_stockage = url_info.get('stockage')
        url_couleur = url_info.get('couleur')

        # Supposons que url_info['gamme'] vous donne "iPhone 15 Pro Max" ou similaire
        full_gamme_name = url_info.get('gamme')

        # Utiliser l'expression régulière pour obtenir seulement "iPhone 15, 14 ou 13"
        match = re.match(r"(iPhone \d{1,2})", full_gamme_name)
        if match:
            url_gamme = match.group(1)
        else:
            url_gamme = full_gamme_name

        for product in response.css('div[data-asin]'):
            full_name = product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product.css('.a-offscreen::text').get()

            if full_name and price:

                # Exemple de nom : "Apple iPhone 15 Plus (128 Go) - Noir"
                gamme = "iPhone"
                name_match = re.search(r'iPhone \d{1,2}( Pro Max| Pro| Plus)?', full_name)
                stockage_match = re.search(r'(\d{1,3}\s?(Go|to|TB|GB))', full_name)
                couleur_match = re.search(r' - (Bleu Alpin|Graphite|Red|Lumière stellaire|Noir sidéral|Violet intense|Minuit|Mauve|Titane \w+|\w+)$', full_name)
                name = name_match.group(0) if name_match else 'Inconnu'
                stockage = stockage_match.group(1) if stockage_match else 'Inconnu'
                couleur = couleur_match.group(1) if couleur_match else 'Inconnu'
                price = price.replace('\u202f', '').replace('\xa0€', '€').strip()
                datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Crée une instance de IphoneItem et attribue les données
                item = IphoneItem()
                item['price'] = price
                item['name'] = name
                item['stockage'] = stockage
                item['gamme'] = gamme
                item['couleur'] = couleur
                item['datetime'] = datetime_now
                
                # Vérifie que les champs ne sont pas 'Inconnu'
                if all(value != 'Inconnu' for value in item.values()):
                    # Comparer avec les informations de l'URL
                    if name == url_model and stockage == url_stockage and couleur == url_couleur:

                        identifiant_unique = f"{url_model}-{url_stockage}-{url_couleur}-{url_gamme}"
                        self.produits[identifiant_unique] = {
                            "nom": url_model,
                            "stockage": url_stockage,
                            "couleur": url_couleur,
                            "prix": item['price'],
                            "gamme": url_gamme,
                            "date": item['datetime']
                        }


                        # Écrire les données dans un fichier JSON avant de fermer
                        self.write_to_json()
                        
                        yield item

    def write_to_json(self):
        # Écrire les données mises à jour dans le fichier JSON
        with open('/app/data_json/donnees_produits.json', 'w', encoding='utf-8') as f:
            json.dump(self.produits, f, ensure_ascii=False, indent=4)


    def close(self, spider, reason):
        
        # Fermer la connexion à MongoDB lorsque le spider est terminé
        self.client.close()



