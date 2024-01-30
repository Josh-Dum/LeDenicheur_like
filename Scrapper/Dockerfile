# Utiliser une image Python officielle comme image de base
FROM python:3.11.7

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires pour l'installation
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exécuter la spider Scrapy
CMD ["scrapy", "crawl", "amazon_spider"]
