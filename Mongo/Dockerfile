# Utiliser une image Python officielle comme base
FROM python:3.11.7

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les fichiers nécessaires pour l'installation
COPY ./requirements_mongo.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements_mongo.txt

# Copier le script bdd.py dans le conteneur
COPY ./Mongo_app/bdd.py .

# Commande pour exécuter bdd.py
CMD ["python", "./bdd.py"]
