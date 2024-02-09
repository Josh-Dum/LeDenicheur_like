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
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
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
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
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
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1 to",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
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
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1 to",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
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
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
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
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Mauve", "prix": "", "date": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 14 Pro",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512GB",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1TB",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 14 Pro Max",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1TB",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                }
            ]
        }
    ]
}

iphone_13_data = {
    "gamme": "iPhone 13",
    "modèles": [
        {
            "nom": "iPhone 13",
            "variantes": [
                {
                    "stockage": "128 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512 Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 13 Mini",
            "variantes": [
                {
                    "stockage": "128Go",
                    "couleurs": [
                        {"couleur": "Red", "prix": "", "date": ""},
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Minuit", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Lumière stellaire", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 13 Pro",
            "variantes": [
                {
                    "stockage": "128Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1To",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                }
            ]
        },
        {
            "nom": "iPhone 13 Pro Max",
            "variantes": [
                {
                    "stockage": "128Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""},
                        {"couleur": "Violet intense", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1To",
                    "couleurs": [
                        {"couleur": "Argent", "prix": "", "date": ""},
                        {"couleur": "Or", "prix": "", "date": ""},
                        {"couleur": "Graphite", "prix": "", "date": ""},
                        {"couleur": "Bleu Alpin", "prix": "", "date": ""}
                    ]
                }
            ]
        }
    ]
}

# models.insert_one(iphone_15_data)

# models.insert_one(iphone_14_data)

models.insert_one(iphone_13_data)



    
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
                    "modèles.$[mod].variantes.$[var].couleurs.$[col].date": produit['date']
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