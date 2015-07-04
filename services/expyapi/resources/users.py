from flask_restful import Resource, reqparse, abort

USER_FIELDS = ['password', 'permissions', 'description']
DEFAULT_USER = {
    'permissions': ['user'],
    'description': 'Meh, thy\'re ok I guess'
}
USERS = {
    'ted': {
        'password': 'coolguy',
        'permissions': ['admin'],
        'description': 'a really cool guy'
    },
    'rich': {
        'password': 'noneed',
        'permissions': ['admin'],
        'description': 'does he need one?'
    }
}

def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} not found".format(user_id))


def update_user_record(args, user_id=None):
    if user_id is None:
        if 'username' not in args:
            abort(400, message='No username specified')
        user_id = args['username']

    current_record = USERS.get(user_id, DEFAULT_USER)
    if args['password'] is not None:
        current_record['password'] = args['password']
    if args['description'] is not None:
        current_record['description'] = args['description']

    USERS[user_id] = current_record
    return USERS[user_id]

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)
parser.add_argument('description', type=str)

# This will be protected by OAuth
class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        return update_user_record(args, user_id), 201

# The list of users will be based on OAuth permissions
class UserList(Resource):
    def get(self):
        return USERS.keys()

    def post(self):
        args = parser.parse_args()
        if 'username' not in args or 'password' not in args:
            abort(400, message="username/password parameter not specified")
        username = args['username']
        if username in USERS.keys():
            abort(409, message="Username {} already exists".format(args['username']))
        return update_user_record(args), 201
