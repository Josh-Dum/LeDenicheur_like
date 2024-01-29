from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Création de la base de données et de la collection
db = client['iphone_db']
models = db['models']







iphone_data = {
    "gamme": "iPhone 15",
    "modèles": [
        {
            "nom": "iPhone 15",
            "variantes": [
                {
                    "stockage": "128Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
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
                    "stockage": "128Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Bleu", "prix": "", "date": ""},
                        {"couleur": "Rose", "prix": "", "date": ""},
                        {"couleur": "Vert", "prix": "", "date": ""},
                        {"couleur": "Jaune", "prix": "", "date": ""},
                        {"couleur": "Noir", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
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
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1To",
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
                    "stockage": "256Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "512Go",
                    "couleurs": [
                        {"couleur": "Titane Naturel", "prix": "", "date": ""},
                        {"couleur": "Titane Bleu", "prix": "", "date": ""},
                        {"couleur": "Titane Noir", "prix": "", "date": ""},
                        {"couleur": "Titane Blanc", "prix": "", "date": ""}
                    ]
                },
                {
                    "stockage": "1To",
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


models.insert_one(iphone_data)
