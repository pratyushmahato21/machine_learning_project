import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "CI CD pipeline has been established"


if __name__ == '__main__':
    app.run(debug=True)
