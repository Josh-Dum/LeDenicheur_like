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

iphone_data = {
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


# Vérifier si les données existent déjà
if models.count_documents({"gamme": "iPhone 15"}) == 0:
    # Insérer les données si elles n'existent pas
    models.insert_one(iphone_data)
else:
    print("Les données existent déjà.")


# # Charger les données du fichier JSON
# with open('/app/data_json/donnees_produits.json', 'r', encoding='utf-8') as file:
#     produits_dict = json.load(file)

# # Mettre à jour MongoDB avec les données chargées
# for identifiant_unique, produit in produits_dict.items():
#     update_result = models.update_one(
#         {"gamme": produit['gamme'], "modèles.nom": produit['nom']},
#         {
#             "$set": {
#                 "modèles.$[mod].variantes.$[var].couleurs.$[col].prix": produit['prix'],
#                 "modèles.$[mod].variantes.$[var].couleurs.$[col].date": produit['date']
#             }
#         },
#         array_filters=[
#             {"mod.nom": produit['nom']},
#             {"var.stockage": produit['stockage']},
#             {"col.couleur": produit['couleur']}
#         ]
#     )
    
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

    if update_result.modified_count == 0:
        print(f"Aucun document mis à jour pour {produit['nom']}.")
    else:
        print(f"Document mis à jour pour {produit['nom']}.")

    print("Base de données mise à jour avec succès.")


while True:
    update_from_json()
    time.sleep(60)