from flask import Flask, request, render_template_string
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch('http://localhost:9200')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_name = request.form.get('search_name', '')
        search_color = request.form.get('search_color', '')
        search_storage = request.form.get('search_storage', '')
        results = search_in_elasticsearch(search_name, search_color, search_storage)
        return render_template_string(SEARCH_RESULTS_TEMPLATE, results=results)
    return render_template_string(HOME_TEMPLATE)

def search_in_elasticsearch(search_name, search_color, search_storage):
    query_filters = []
    
    if search_name:
        query_filters.append({"match": {"nom": search_name}})
    if search_color:
        query_filters.append({"match": {"couleur": search_color}})
    if search_storage:
        query_filters.append({"match": {"stockage": search_storage}})
    
    body = {
        "query": {
            "bool": {
                "must": query_filters
            }
        },
        "size": 10
    }

    response = es.search(index="iphone_index", body=body)
    return [hit["_source"] for hit in response['hits']['hits']]

# Le template de la page d'accueil doit être mis à jour pour inclure les champs de recherche supplémentaires
HOME_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Recherche</title></head>
<body>
  <h2>Recherche iPhone</h2>
  <form method="post">
    <input type="text" name="search_name" placeholder="Nom" />
    <input type="text" name="search_color" placeholder="Couleur" />
    <input type="text" name="search_storage" placeholder="Stockage" />
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
      <li>Gamme: {{ result['gamme'] }}, Nom: {{ result['nom'] }}, Stockage: {{ result['stockage'] }}, Couleur: {{ result['couleur'] }}, Prix: {{ result['prix'] }}, Date: {{ result['date'] }}</li>
    {% endfor %}
  </ul>
  <a href="/">Nouvelle recherche</a>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
