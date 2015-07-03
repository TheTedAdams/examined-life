from flask import Flask

mod = ('api', __name__)


@mod.route('/')
def api_root():
    return 'Hello from the analytics api'


@mod.route('/oauth2/token')
def get_oauth2_token():
    return 'Did you really think I would give you one?'


@mod.route('/oauth2/authorize')
def authorize_oauth2_token():
    return 'Nope, you\'re not, I guarantee it'

