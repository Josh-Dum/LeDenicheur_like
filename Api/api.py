from flask import Flask, request, render_template_string
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch('http://elasticsearch:9200')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_name = request.form.get('search_name', '')
        search_color = request.form.get('search_color', '')
        search_storage = request.form.get('search_storage', '')
        price_min = request.form.get('price_min', '')
        price_max = request.form.get('price_max', '')

        # Convertir price_min et price_max en float si elles ne sont pas vides
        if price_min:
            price_min = float(price_min)
        else:
            price_min = None

        if price_max:
            price_max = float(price_max)
        else:
            price_max = None

        results = search_in_elasticsearch(search_name, search_color, search_storage, price_min, price_max)
        return render_template_string(SEARCH_RESULTS_TEMPLATE, results=results)
    return render_template_string(HOME_TEMPLATE)

def search_in_elasticsearch(search_name, search_color, search_storage, price_min, price_max):
    query_filters = []

    if search_name:
        query_filters.append({"match": {"nom": search_name}})
    if search_color:
        query_filters.append({"match": {"couleur": search_color}})
    if search_storage:
        query_filters.append({"match": {"stockage": search_storage}})
    if price_min is not None or price_max is not None:
        price_range_filter = {"range": {"prix": {}}}
        if price_min is not None:
            price_range_filter["range"]["prix"]["gte"] = price_min
        if price_max is not None:
            price_range_filter["range"]["prix"]["lte"] = price_max
        query_filters.append(price_range_filter)

    body = {
        "query": {
            "bool": {
                "must": query_filters
            }
        },
        "size": 10
    }

    print("Requête envoyée à Elasticsearch:", body)  # Instruction d'impression pour déboguer
    response = es.search(index="iphone_index", body=body)
    return [hit["_source"] for hit in response['hits']['hits']]

HOME_TEMPLATE = '''
<!doctype html>
<html lang="fr">
<head>
    <title>Trouve ton Iphone, Au meilleur prix</title>
    <!-- Intégration de Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding-top: 10vh; /* Ajuste le titre vers le haut */
            margin: 0; /* Enlève la marge par défaut du body */
            height: 100vh; /* Hauteur de la fenêtre */
            display: flex;
            flex-direction: column;
            background: linear-gradient(to bottom, #ffffff 0%, #e6f0fa 100%); /* Dégradé de blanc à bleu clair */
        }
        .search-container {
            text-align: center; /* Centre le formulaire */
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center; /* Centrer le formulaire verticalement */
        }
        .form-group {
            margin-bottom: 1rem; /* Espacement entre les champs */
        }
        .btn {
            margin-top: 1rem; /* Espacement au-dessus du bouton */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transition pour les effets */
        }
        .btn:hover {
            transform: scale(1.05); /* Agrandissement au survol */
            box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Ombre portée */
        }
        .form-control:hover {
            border-color: #007bff; /* Couleur de la bordure au survol */
            box-shadow: inset 0 1px 1px rgba(0,0,0,0.075), 0 0 8px rgba(102, 175, 233, 0.6); /* Ombre interne */
        }
        .double-input {
            display: flex;
            gap: 1rem; /* Espace entre les deux inputs */
        }
        .double-input > div {
            flex: 1; /* Les inputs prennent la même largeur */
        }
        h2 {
            margin-bottom: 10rem; /* Ajustez cette valeur pour augmenter ou diminuer l'espace */
            transition: transform 0.3s ease; /* Animation de base pour le survol */
        }
        h2:hover {
            transform: scale(1.05); /* Agrandit légèrement le titre */
            color: #007bff; /* Change la couleur pour correspondre au bouton principal de Bootstrap */
        }

        footer {
            text-align: center;
            padding: 1rem 0;
            font-size: 0.8em;
            color: #6c757d; /* Couleur Bootstrap pour le texte plus clair */
        }
        
    </style>
</head>
<body>
    <div class="container">
        <div class="search-container">
            <h2>Trouve ton Iphone, au meilleur prix</h2>
            <form method="post">
                <div class="form-group">
                    <input class="form-control" type="text" name="search_name" placeholder="Ton modèle">
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="search_color" placeholder="Ta couleur">
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="search_storage" placeholder="Ton stockage">
                </div>
                <div class="double-input">
                    <div>
                        <input class="form-control" type="number" name="price_min" placeholder="Prix Mini" step="0.01">
                    </div>
                    <div>
                        <input class="form-control" type="number" name="price_max" placeholder="Prix Maxi" step="0.01">
                    </div>
                </div>
                <button type="submit" class="btn btn-primary">Chercher</button>
            </form>
        </div>
    </div>
    <footer>
        <p>Le scraping des données se fait uniquement sur Amazon pour le moment.</p>
    </footer>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


'''

SEARCH_RESULTS_TEMPLATE = '''
<!doctype html>
<html lang="fr">
<head>
    <title>Résultats</title>
    <!-- Intégration de Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to bottom, #ffffff 0%, #e6f0fa 100%);
            padding-top: 5vh;
        }
        .list-group-item:hover {
            transform: scale(1.02); /* Effet de zoom au survol */
            background-color: #f8f9fa; /* Changement de fond pour un effet subtil */
        }
        .list-group-item {
            transition: transform .2s ease, background-color .2s ease; /* Animation fluide */
        }
        h2 {
            text-align: center; /* Centre le titre */
            margin-bottom: 20px; /* Espacement avant la liste */
        }
        .btn-primary:hover {
            box-shadow: 0 0 8px rgba(0,123,255,.5); /* Ombre douce au survol */
        }
        .nom {
            color: #007bff; /* Couleur bleue pour le nom */
        }
        .prix {
            font-weight: bold; /* Mise en gras du prix */
        }
    </style>
</head>
<body>
<div class="container mt-5">
    <h2>Résultats de la recherche</h2>
    {% if results %}
        <div class="list-group">
            {% for result in results %}
                <div class="list-group-item flex-column align-items-start">
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1 nom">{{ result['nom'] }}</h5>
                        <small>{{ result['date'] }}</small>
                    </div>
                    <p class="mb-1">Stockage: {{ result['stockage'] }} | Couleur: {{ result['couleur'] }} | <span class="prix">{{ result['prix'] }} €</span></p>
                    <small>Gamme: {{ result['gamme'] }}</small>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <p class="text-center">Aucun résultat trouvé.</p>
    {% endif %}
    <div class="text-center mt-3">
        <a href="/" class="btn btn-primary">Nouvelle recherche</a>
    </div>
</div>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
