import scrapy
import pymongo
from scrapy.utils.project import get_project_settings
import urllib.parse
from scrapy_app.items import IphoneItem 
from datetime import datetime
import pymongo
import os
import re


class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.fr']
    # start_urls = ['https://www.amazon.fr/s?k=iphone15+pro+1To+titane+naturel']


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


        for product in response.css('div[data-asin]'):
            full_name = product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product.css('.a-offscreen::text').get()

            if full_name and price:

                # Exemple de nom : "Apple iPhone 15 Plus (128 Go) - Noir"
                gamme = "iPhone"
                name_match = re.search(r'iPhone \d{1,2}( Pro Max| Pro| Plus)?', full_name)
                stockage_match = re.search(r'(\d{1,3} (Go|to))', full_name)
                couleur_match = re.search(r' - (Titane \w+|\w+)$', full_name)
                name = name_match.group(0) if name_match else 'Inconnu'
                stockage = stockage_match.group(1) if stockage_match else 'Inconnu'
                couleur = couleur_match.group(1) if couleur_match else 'Inconnu'
                price = price.replace('\u202f', '').replace('\xa0€', '€').strip()
                datetime_now = datetime.now().strftime("%Y-%m-%d")

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
                        # Mettre à jour la base de données
                        self.logger.info(f"Mise à jour de la base de données pour : {url_model}, {url_stockage}, {url_couleur}")

                        update_result = self.models.update_one(
                            {"nom": url_model, "stockage": url_stockage, "couleur": url_couleur},
                            {"$set": {"prix": item['price'], "date": item['datetime']}}
                        )

                        # Vérifier si la mise à jour a été effectuée
                        if update_result.matched_count > 0:
                            self.logger.info("Mise à jour réussie.")
                        else:
                            self.logger.warning("Aucune correspondance trouvée pour la mise à jour.")

                        print(url_couleur)
                        print(url_model)

                        yield item
                        break  # Arrêtez après avoir trouvé et mis à jour l'item correspondant
                # else:
                #     self.logger.info(f"Information manquante pour le produit : {product.attrib['data-asin']}")
            # else:
            #     self.logger.info(f"Produit manquant : {product.attrib['data-asin']}")


    def close(self, spider, reason):
        # Fermer la connexion à MongoDB lorsque le spider est terminé
        self.client.close()



