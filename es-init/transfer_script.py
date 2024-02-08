from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers

# Connexion à MongoDB
mongo_client = MongoClient('mongodb://mongo:27017/')
mongo_db = mongo_client['iphone_db']
mongo_collection = mongo_db['models']  # Remplacez par le nom de votre collection

# Connexion à Elasticsearch
es = Elasticsearch('http://localhost:9200')  # Assurez-vous que l'adresse correspond à votre configuration

# Création d'un index Elasticsearch si nécessaire
if not es.indices.exists(index="iphone_index"):
    es.indices.create(index="iphone_index")

# Récupération des documents de MongoDB et indexation dans Elasticsearch
docs = mongo_collection.find()
actions = [
    {
        "_index": "iphone_index",
        "_source": doc
    }
    for doc in docs
]

helpers.bulk(es, actions)
