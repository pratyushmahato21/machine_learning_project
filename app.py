import flask
from housing.logger import logging
from housing.exception import HousingException

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info(" We are testing logging module")
    return "CI CD pipeline has been established"


if __name__ == '__main__':
    app.run(debug=True)
