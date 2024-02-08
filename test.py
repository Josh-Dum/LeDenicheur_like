from flask import Flask, request, render_template_string
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch('http://localhost:9200')

# Page d'accueil avec la barre de recherche
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['search']
        results = search_in_elasticsearch(query)
        return render_template_string(SEARCH_RESULTS_TEMPLATE, results=results)
    return render_template_string(HOME_TEMPLATE)

def search_in_elasticsearch(query):
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["nom", "modèles.nom", "modèles.variantes.stockage", "modèles.variantes.couleurs.couleur", "modèles.variantes.couleurs.prix"]
            }
        },
        "size": 10
    }
    response = es.search(index="iphone_index", body=body)
    return [hit["_source"] for hit in response['hits']['hits']]

HOME_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Recherche</title></head>
<body>
  <h2>Recherche iPhone</h2>
  <form method="post">
    <input type="text" name="search" />
    <input type="submit" value="Chercher" />
  </form>
</body>
</html>
'''

SEARCH_RESULTS_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Résultats</title></head>
<body>
  <h2>Résultats de la recherche</h2>
  <ul>
    {% for result in results %}
      <li>{{ result }}</li>
    {% endfor %}
  </ul>
  <a href="/">Nouvelle recherche</a>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
