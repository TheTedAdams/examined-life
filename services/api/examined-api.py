from flask import Flask

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Hello from the analytics api'


@app.route('/oauth2/token')
def get_oauth2_token():
    return 'Did you really think I would give you one?'


@app.route('/oauth2/authorize')
def authorize_oauth2_token():
    return 'Nope, you\'re not, I guarantee it'


if __name__ == '__main__':
    app.run(debug=True)
