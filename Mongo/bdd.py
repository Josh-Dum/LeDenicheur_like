from pymongo import MongoClient
from datetime import datetime
import urllib.parse
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


# Vérifier si les données existent déjà
if models.count_documents({"gamme": "iPhone 15"}) == 0:
    # Insérer les données si elles n'existent pas
    models.insert_one(iphone_data)
else:
    print("Les données existent déjà.")




# Récupération de la date actuelle
current_date = datetime.now().strftime("%Y-%m-%d")
urls = []
# Génération des URLs pour le scraping
for model in models.find({}):
    gamme = model["gamme"]
    for modele in model["modèles"]:
        nom_modele = modele["nom"]
        for variante in modele["variantes"]:
            stockage = variante["stockage"]
            for couleur in variante["couleurs"]:
                couleur_nom = couleur["couleur"]
                # Construction de l'URL pour Amazon
                query = f"{nom_modele} {couleur_nom} {stockage}".replace(" ", "+")
                url = f"https://www.amazon.fr/s?k={urllib.parse.quote(query)}"
                urls.append(url)
                # Ajout de la date actuelle
                couleur["date"] = current_date

print(urls)
print(len(urls))
print(current_date)