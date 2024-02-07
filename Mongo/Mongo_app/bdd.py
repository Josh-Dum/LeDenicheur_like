from pymongo import MongoClient
from datetime import datetime
import urllib.parse

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


