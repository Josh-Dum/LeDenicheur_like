# LEDENICHEUR_LIKE

LEDENICHEUR_LIKE est un projet conçu pour faciliter la recherche des iPhones les moins chers sur Amazon en utilisant une architecture microservices. Le projet intègre Flask, MongoDB, Elasticsearch, et Scrapy pour collecter, stocker, et rechercher efficacement les données sur les produits.

## Prérequis

- Docker
- Docker Compose

## Installation

Pour lancer l'ensemble du projet, suivez ces étapes :

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous que Docker et Docker Compose sont installés et fonctionnels.
3. Dans le répertoire racine du projet, exécutez la commande :

```
docker-compose up --build
```


Cela construira et lancera tous les services nécessaires définis dans le fichier `docker-compose.yml`.

## Utilisation

Une fois que tous les services sont lancés, vous pouvez accéder à l'interface utilisateur Flask à l'adresse suivante :

```
http://localhost:5000
```

Pour effectuer une recherche, assurez-vous d'attendre quelques secondes après le lancement des conteneurs pour que le service Elasticsearch soit pleinement opérationnel.

## Architecture et Choix Techniques

Le projet est divisé en plusieurs composants clés :

- **Api/** : Un service Flask fournissant une interface utilisateur pour effectuer des recherches sur les produits. Utilise Bootstrap pour une meilleure ergonomie.
- **es-init/** : Un service pour initialiser Elasticsearch avec des données provenant de MongoDB et les mettre à jour régulièrement.
- **Mongo/** : Contient les données des produits et un script d'initialisation pour peupler MongoDB.
- **Scrapper/** : Un service Scrapy pour extraire les informations des produits des gammes iPhone 15 et 14 sur Amazon.

### Docker Compose

`docker-compose.yml` orchestre le déploiement de tous les services, en établissant les dépendances nécessaires entre eux pour un fonctionnement harmonieux.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le dépôt.
2. Créez votre branche de fonctionnalités (`git checkout -b feature/AmazingFeature`).
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Poussez vers la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

## Contact

Si vous avez des questions ou des suggestions concernant ce projet, n'hésitez pas à ouvrir un issue dans ce dépôt GitHub.



