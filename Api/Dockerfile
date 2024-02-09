# Utiliser une image Python officielle comme base
FROM python:3.11.7

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires pour l'installation
COPY . /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Commande pour exécuter bdd.py
CMD ["python", "-u", "api.py"]