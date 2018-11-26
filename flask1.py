from flask import Flask, render_template, jsonify
app = Flask(__name__, template_folder='.')


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/")
def hello():
    user = {'username': 'Miguel'}
    return render_template('index.html', user=user)

@app.route('/index')
def index():
    return "<a href='/'>back to main...</a>"

@app.route('/api/books', methods=['GET'])
def getBooks():
    return jsonify(books)
