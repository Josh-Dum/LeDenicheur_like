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


# def mongo_doc_to_es(doc):
#     # Transforme le document MongoDB en JSON
#     return json.loads(json_util.dumps(doc))

# def generate_es_documents(docs):
#     for doc in docs:
#         gamme = doc['gamme']
#         for modele in doc['modèles']:
#             nom_modele = modele['nom']
#             for variante in modele['variantes']:
#                 stockage = variante['stockage']
#                 for couleur in variante['couleurs']:

#                     # Supprimer les symboles de monnaie et convertir en nombre
#                     prix_texte = couleur['prix'].replace('€', '').replace(',', '.')
#                     try:
#                         prix = float(prix_texte.strip())
#                     except ValueError:
#                         prix = 0.0  # ou une autre valeur par défaut en cas d'erreur

#                     print(prix)
#                     # Créer un document pour chaque variante de couleur
#                     doc_es = {
#                         'gamme': gamme,
#                         'nom': nom_modele,
#                         'stockage': stockage,
#                         'couleur': couleur['couleur'],
#                         'prix': prix,
#                         'date': couleur['date']
#                     }
#                     yield {
#                         "_index": "iphone_index",
#                         "_source": doc_es
#                     }
                    

# # Indexation des documents dans Elasticsearch
# docs_mongo = mongo_collection.find()
# actions = list(generate_es_documents(docs_mongo))
# helpers.bulk(es, actions)
    
def generate_es_documents(docs):
    for doc in docs:
        gamme = doc['gamme']
        for modele in doc['modèles']:
            nom_modele = modele['nom']
            for variante in modele['variantes']:
                stockage = variante['stockage']
                for couleur in variante['couleurs']:

                    # Supprimer les symboles de monnaie et convertir en nombre
                    prix_texte = couleur['prix'].replace('€', '').replace(',', '.')
                    try:
                        prix = float(prix_texte.strip())
                    except ValueError:
                        prix = 0.0  # ou une autre valeur par défaut en cas d'erreur

                    
                    # Créer un document pour chaque variante de couleur
                    doc_es = {
                        'gamme': gamme,
                        'nom': nom_modele,
                        'stockage': stockage,
                        'couleur': couleur['couleur'],
                        'prix': prix,
                        'date': couleur['date']
                    }
                    yield {
                        "_index": "iphone_index",
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