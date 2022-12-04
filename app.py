import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Starting ML project"


if __name__ == '__main__':
    app.run(debug=True)
