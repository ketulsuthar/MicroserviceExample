from flask import Flask
app = Flask(__name__)


@app.rout('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')