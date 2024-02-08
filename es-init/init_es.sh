#!/bin/bash

# Attendre qu'Elasticsearch soit disponible
while ! curl -s http://elasticsearch:9200/_cluster/health > /dev/null; do
  echo "En attente d'Elasticsearch..."
  sleep 1
done

echo "Elasticsearch est prêt."

# Exécuter le script de transfert de données
python /app/transfer_script.py
