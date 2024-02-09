# LEDENICHEUR_LIKE

LEDENICHEUR_LIKE est une application conçue pour recueillir et fournir des informations sur différents produits à travers une API. Elle utilise un scraper pour collecter les données, les stocke dans une base de données MongoDB et offre une interface de recherche via Elasticsearch.

## Structure du Projet

- `Api/`: Contient le code source de l'API RESTful pour interagir avec l'application.
- `es-init/`: Scripts et configurations pour initialiser Elasticsearch.
- `Mongo/`: Scripts pour générer et gérer la base de données MongoDB.
- `Scrapper/`: Contient le scraper qui utilise Scrapy pour recueillir les données des produits.

## Installation

Ce projet utilise Docker et `docker-compose` pour faciliter l'installation et la configuration.

1. Clonez le dépôt :
```
git clone [url-du-dépôt]
```
2. Construisez les images Docker et lancez les conteneurs :
```
docker-compose up --build
```

## Usage

Une fois que les conteneurs sont lancés, l'API peut être accessible à l'adresse suivante : `http://localhost:port/` où `port` est le port configuré dans le fichier `docker-compose.yml`.

## Développement

- Pour ajouter/modifier les spiders : 
- Naviguez vers `Scrapper/scrapy_app/spiders/`
- Utilisez `scrapy genspider [nom_du_spider] [domaine]` pour générer un nouveau spider.
- Modifiez `items.py` pour définir les modèles de données à collecter.

- Pour la gestion de la base de données :
- Le script `bdd.py` dans `Mongo/Mongo_app/` contient la logique de connexion et les opérations de la base de données.

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre vos pull requests à la branche `develop`.

## Licence

Ce projet est sous licence [Insérer la licence ici].

## Auteurs

- [Votre Nom] - Développement initial

## Remerciements

Merci à tous ceux qui ont contribué au projet, y compris les collaborateurs et les membres de la communauté qui ont soumis des bugs et des suggestions.

---

Pour plus d'informations sur la configuration spécifique, les méthodes de lancement détaillées ou les choix techniques, veuillez consulter la documentation technique complémentaire disponible dans le dépôt.
