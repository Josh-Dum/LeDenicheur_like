from pymongo import MongoClient
from datetime import datetime
import urllib.parse
import json
import time

# Connexion à MongoDB
client = MongoClient('mongodb://mongo:27017/')

# Création de la base de données et de la collection
db = client['iphone_db']
models = db['models']



# Vider la collection
models.delete_many({})

iphone_15_data = {
    "gamme": "iPhone 15",
    "modèles": [
        {
            "nom": "iPhone 15",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 15 Plus",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Rose", "prix": "", "date": "", "link": ""},
                        {"couleur": "Vert", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Noir", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 15 Pro",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "1 to",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 15 Pro Max",
            "variantes": [
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "1 to",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": "", "link": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        }
    ]
}

iphone_14_data = {
    "gamme": "iPhone 14",
    "modèles": [
        {
            "nom": "iPhone 14",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 14 Plus",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "(Product) Red", "prix": "", "date": "", "link": ""},
                        {"couleur": "Bleu", "prix": "", "date": "", "link": ""},
                        {"couleur": "Minuit", "prix": "", "date": "", "link": ""},
                        {"couleur": "Jaune", "prix": "", "date": "", "link": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": "", "link": ""},
                        {"couleur": "Mauve", "prix": "", "date": "", "link": ""}
                    ]
                }
            ]
        },
    ]
}


models.insert_one(iphone_15_data)

models.insert_one(iphone_14_data)




    
def update_from_json():
    # Charger les données du fichier JSON
    with open('/app/data_json/donnees_produits.json', 'r', encoding='utf-8') as file:
        produits_dict = json.load(file)

    # Mettre à jour MongoDB avec les données chargées
    for identifiant_unique, produit in produits_dict.items():
        update_result = models.update_one(
            {"gamme": produit['gamme'], "modèles.nom": produit['nom']},
            {
                "$set": {
                    "modèles.$[mod].variantes.$[var].couleurs.$[col].prix": produit['prix'],
                    "modèles.$[mod].variantes.$[var].couleurs.$[col].date": produit['date'],
                    "modèles.$[mod].variantes.$[var].couleurs.$[col].link": produit['link']
                }
            },
            array_filters=[
                {"mod.nom": produit['nom']},
                {"var.stockage": produit['stockage']},
                {"col.couleur": produit['couleur']}
            ]
        )

    print("Base de données mise à jour avec succès.")


while True:
    update_from_json()
    time.sleep(60)