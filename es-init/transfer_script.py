from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers
from bson import json_util
import json

# Connexion à MongoDB
mongo_client = MongoClient('mongodb://mongo:27017/')
mongo_db = mongo_client['iphone_db']
mongo_collection = mongo_db['models']  # Remplacez par le nom de votre collection

# Connexion à Elasticsearch
es = Elasticsearch('http://elasticsearch:9200')  # Assurez-vous que l'adresse correspond à votre configuration

# Création d'un index Elasticsearch si nécessaire
if not es.indices.exists(index="iphone_index"):
    es.indices.create(index="iphone_index")

# Fonction pour convertir de MongoDB vers un format compatible JSON pour Elasticsearch
def mongo_doc_to_es(doc):
    # Utilise json_util pour convertir le document MongoDB en JSON
    doc_json = json.loads(json_util.dumps(doc))
    # Supprimez les clés non nécessaires ou ajustez le document ici si nécessaire
    doc_json.pop('_id', None)  # Supprime l'_id MongoDB s'il n'est pas nécessaire dans Elasticsearch
    return doc_json

# Récupération des documents de MongoDB et indexation dans Elasticsearch
docs = mongo_collection.find()
actions = [
    {
        "_index": "iphone_index",
        "_source": mongo_doc_to_es(doc)
    }
    for doc in docs
]

helpers.bulk(es, actions)
