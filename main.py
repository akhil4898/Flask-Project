from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page....This is all about this page...fine"


if __name__ == '__main__':
    app.run(debug=True)

