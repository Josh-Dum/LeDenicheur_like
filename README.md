# LEDENICHEUR_LIKE

LEDENICHEUR_LIKE est un projet conçu pour faciliter la recherche des iPhones les moins chers en temps réel (actualisation toutes les minutes) sur Amazon. Le projet intègre Flask, MongoDB, Elasticsearch, et Scrapy pour collecter, stocker, et rechercher efficacement les données sur les produits.

## Prérequis

- Docker (4.27.1)
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

## Informations Importantes Concernant le Scrapping des iPhones

### Erreurs de Scrapping et Blocage par Amazon

Lors de l'utilisation de notre outil de scrapping pour collecter des données sur les iPhones, il est possible que vous rencontriez des erreurs fréquentes, notamment des erreurs `HTTP 503 Service Unavailable`. Ces erreurs sont généralement le résultat de restrictions imposées par Amazon pour prévenir le scrapping automatisé de leurs pages web.

Si vous constatez que le service de scrapping est souvent en état `exited`, cela peut également indiquer que nos tentatives de scrapping ont été bloquées par Amazon. Ces mesures de sécurité peuvent varier dans leur sévérité et leur durée, mais elles sont mises en place pour protéger le contenu du site d'Amazon contre l'extraction non autorisée.

### Gestion de l'Heure

Veuillez noter que toutes les heures enregistrées dans nos logs et les données scrapées sont en heure britannique (GMT/UTC+0). Ceci signifie qu'il peut y avoir un décalage d'une heure par rapport à l'heure de Paris (CET/UTC+1) pendant une partie de l'année. Assurez-vous de prendre en compte ce décalage lors de l'interprétation des données.

## Recommandations

Pour éviter ces problèmes, nous recommandons d'adopter les pratiques suivantes :

- **Relancer le projet** : Avoir le Scrapping en temps réel permet une actualisation toutes les minutes de la base de donnée Mongo et de elastic search. Vous pourrez constatez ainsi une actualisation sur Flask minute par minute. 
- **Ralentir la fréquence de scrapping** : En espaçant les requêtes de scrapping, on a déjà réduit le risque de détection et de blocage par les mécanismes anti-scrapping d'Amazon.
- **Scrapping pendant les heures creuses** : Tenter de scraper pendant les périodes où les serveurs sont moins sollicités peut réduire les chances d'être bloqué.

## Architecture et Choix Techniques

Notre projet est conçu autour d'une architecture microservices, en effet chaque services (détaillés plus bas) ont des taches bien précises.

### Api/

- **Technologie** : Le service API utilise Flask, un micro-framework Python qui offre la flexibilité nécessaire pour développer des applications web rapidement et avec un minimum de code. Flask a été choisi pour sa simplicité et sa capacité à s'intégrer facilement avec d'autres services comme Elasticsearch.
- **Rôle** : Ce service agit comme le point d'entrée pour les utilisateurs, fournissant une interface web pour effectuer des recherches sur les produits. L'utilisation de Bootstrap améliore l'expérience utilisateur en proposant une interface propre et réactive.
- **Communication avec Elasticsearch** : L'API communique directement avec Elasticsearch pour récupérer les informations sur les produits en fonction des requêtes des utilisateurs. Ce choix permet d'exploiter la puissance de recherche d'Elasticsearch, offrant des résultats rapides et pertinents.

### es-init/

- **Scripts d'Initialisation** : Les scripts `init_es.sh` et `transfer_script.py` travaillent ensembles pour préparer et maintenir à jour l'index Elasticsearch. Le script Bash attend qu'Elasticsearch soit prêt avant de lancer le script Python, qui transfère ensuite les données de MongoDB vers Elasticsearch. La base de donnée est mise à jour chaque minute.
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

## Contact

- **Joshua Dumont**
  - **Gmail** : [dumonthoshua@gmail.com](mailto:dumonthoshua@gmail.com)

- **Eliott Vigier**
  - **Gmail** : [eliott.vigier@edu.esiee.fr](mailto:eliott.vigier@edu.esiee.fr)

Si vous avez des questions ou des suggestions concernant ce projet, n'hésitez pas à nous contacter



