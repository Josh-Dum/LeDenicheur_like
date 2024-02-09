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

Le projet "LEDENICHEUR_LIKE" est conçu autour d'une architecture microservices, optimisée pour la scalabilité, la modularité et la facilité de maintenance. Chaque composant du système a été choisi et configuré pour répondre au mieux aux besoins spécifiques du projet, depuis la collecte des données jusqu'à la présentation des informations aux utilisateurs.

### Api/

- **Technologie** : Le service API utilise Flask, un micro-framework Python qui offre la flexibilité nécessaire pour développer des applications web rapidement et avec un minimum de code. Flask a été choisi pour sa simplicité et sa capacité à s'intégrer facilement avec d'autres services comme Elasticsearch.
- **Rôle** : Ce service agit comme le point d'entrée pour les utilisateurs, fournissant une interface web pour effectuer des recherches sur les produits. L'utilisation de Bootstrap améliore l'expérience utilisateur en proposant une interface propre et réactive.
- **Communication avec Elasticsearch** : L'API communique directement avec Elasticsearch pour récupérer les informations sur les produits en fonction des requêtes des utilisateurs. Ce choix permet d'exploiter la puissance de recherche d'Elasticsearch, offrant des résultats rapides et pertinents.

### es-init/

- **Scripts d'Initialisation** : Les scripts `init_es.sh` et `transfer_script.py` travaillent de concert pour préparer et maintenir à jour l'index Elasticsearch. Le script Bash attend qu'Elasticsearch soit prêt avant de lancer le script Python, qui transfère ensuite les données de MongoDB vers Elasticsearch.
- **Choix d'Elasticsearch** : Elasticsearch est utilisé pour sa capacité à effectuer des recherches complexes et à grande échelle. Son système d'indexation permet des requêtes rapides, ce qui est essentiel pour fournir une expérience utilisateur fluide lors de la recherche de produits.

### Mongo/

- **Stockage des Données** : MongoDB, une base de données NoSQL, est utilisée pour stocker les données des produits de manière flexible. Les documents JSON permettent une structure de données complexe, idéale pour les informations détaillées des produits.
- **Génération et Mise à Jour des Données** : Le dossier `data_json` et le script `bdd.py` sont essentiels pour initialiser la base de données avec les données des produits et les maintenir à jour. MongoDB a été choisi pour sa facilité d'intégration avec des applications Python et sa capacité à gérer de grands volumes de données.

### Scrapper/

- **Scrapy pour le Web Scraping** : Scrapy, un framework de scraping web, est utilisé pour extraire les données des produits depuis les pages d'Amazon. Scrapy a été sélectionné pour sa robustesse, sa facilité d'utilisation et sa capacité à traiter des données web à grande échelle.
- **Traitement des Données** : Après le scraping, les données sont traitées et formatées en JSON pour être compatibles avec MongoDB. Ce prétraitement est crucial pour assurer l'intégrité et la structure des données stockées.

### docker-compose.yml

- **Orchestration des Services** : Docker Compose est utilisé pour définir et exécuter l'ensemble de l'architecture en conteneurs Docker. Cette approche garantit la cohérence des environnements de développement, de test et de production, simplifie le déploiement et la gestion des services.
- **Dépendances et Orchestration** : Le fichier `docker-compose.yml` configure les dépendances entre services, assurant que chaque service est lancé dans l'ordre approprié et peut communiquer avec les autres. Par exemple, le service `es-init` ne démarre qu'après `elasticsearch`, garantissant que la base de données est prête à recevoir des données.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le dépôt.
2. Créez votre branche de fonctionnalités (`git checkout -b feature/AmazingFeature`).
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Poussez vers la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

## Contact

Si vous avez des questions ou des suggestions concernant ce projet, n'hésitez pas à ouvrir un issue dans ce dépôt GitHub.



