from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers
from bson import json_util
import json
import time 

# Connexion à MongoDB
mongo_client = MongoClient('mongodb://mongo:27017/')
mongo_db = mongo_client['iphone_db']
mongo_collection = mongo_db['models']

# Connexion à Elasticsearch
es = Elasticsearch('http://elasticsearch:9200')

# Assurez-vous que l'adresse correspond à votre configuration
if not es.indices.exists(index="iphone_index"):
    es.indices.create(index="iphone_index")


def generate_es_documents(docs):
    for doc in docs:
        gamme = doc['gamme']
        for modele in doc['modèles']:
            nom_modele = modele['nom']
            for variante in modele['variantes']:
                stockage = variante['stockage']
                for couleur in variante['couleurs']:

                    # Supprimer les symboles de monnaie et convertir en nombre
                    prix_texte = couleur['prix'].replace('€', '').replace(',', '.').strip()
                    try:
                        prix = float(prix_texte)
                    except ValueError:
                        prix = None  # ou une autre valeur par défaut en cas d'erreur

                    unique_id = f"{nom_modele}_{stockage}_{couleur['couleur']}".replace(' ', '_').lower()  # Générer un ID unique
                    # Créer un document pour chaque variante de couleur
                    doc_es = {
                        'gamme': gamme,
                        'nom': nom_modele,
                        'stockage': stockage,
                        'couleur': couleur['couleur'],
                        'prix': prix,
                        'date': couleur['date'],
                        'link': couleur['link']
                    }
                    yield {
                        "_index": "iphone_index",
                        "_id": unique_id,  # Utiliser l'ID unique généré
                        "_source": doc_es
                    }


def update_es_from_mongo():
    docs_mongo = mongo_collection.find()
    actions = generate_es_documents(docs_mongo)
    helpers.bulk(es, actions)
    print("Elasticsearch mis à jour avec succès.")


while True:
    update_es_from_mongo()
    time.sleep(60)