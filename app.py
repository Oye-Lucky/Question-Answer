from json import JSONEncoder
from flask import Flask, request

import chocolateo
import commandscrape

app = Flask(__name__)


@app.route('/')
def home():
    return app.response_class(
        response='Asteroid is working',
        status=200,
        mimetype='application/json'
    )


@app.route('/api/answer')
def answer():
    result = chocolateo.web_scrape(request.args.get("text"))

    return app.response_class(
        response=JSONEncoder().encode({
            "answer": result[0],
            "source": result[1]
        }),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/info')
def info():
    return app.response_class(
        response=JSONEncoder().encode({
            "answer": chocolateo.bingScrape(request.args.get('text')),
        }),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/command/')
def commandScrape():
    return app.response_class(
        response=JSONEncoder().encode({
            "result": commandscrape.command_scrape(request.args.get('text')),
        }),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run()
