from tables import create_passwords_table, create_users_table
from flask import Flask, request, Response
from functools import wraps
from httpHelpers import stringToJsonError
from dbHelpers import create_connection, create_table, create_password, get_passwords, delete_password, update_password, get_user, create_user, update_user, delete_user, get_user_by_email_and_pass
import jwt

app = Flask(__name__)


def main():
    create_table(create_passwords_table)
    create_table(create_users_table)


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            data = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.exceptions.ExpiredSignatureError:
            return Response("tokenExpired", 401)
        except:
            return Response("tokenInvalid", 401)
        return f(*args, **kwargs)
    return wrapper


def user_idFromAuth():
    try:
        token = request.headers.get('Authorization')
        data = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return None
    return data['user_id']


@app.route("/auth/login", methods=['POST'])
def login():
    user = get_user_by_email_and_pass(
        request.json['email'], request.json['password'])
    if user is None:
        return Response('loginInvalid', 401)
    else:
        encoded_jwt = jwt.encode(
            {'user_id': user['user_id']}, 'secret', algorithm='HS256').decode('utf-8')
        return {
            "jwt": encoded_jwt
        }


@app.route('/users', methods=['GET'])
@authenticate
def getUser():
    return get_user(user_idFromAuth())


@app.route('/users', methods=['POST'])
def createUser():
    return create_user((request.json['email'], request.json['password']))


@app.route('/users', methods=['PUT'])
@authenticate
def updateUser():
    return update_user(request.json['email'], request.json['password'], user_idFromAuth())


@app.route('/users', methods=['DELETE'])
@authenticate
def deleteUser():
    return delete_user(user_idFromAuth())


@app.route('/passwords', methods=['GET'])
@authenticate
def getPasswords():
    return get_passwords(user_idFromAuth())


@app.route('/passwords', methods=['POST'])
@authenticate
def createPassword():
    return create_password((user_idFromAuth(), request.json['username'], request.json['password'], request.json['website']))


@app.route('/passwords', methods=['PUT'])
@authenticate
def updatePassword():
    return update_password(request.json['username'], request.json['password'], request.json['website'], request.json['id'], user_idFromAuth())


@app.route('/passwords/<id>', methods=['DELETE'])
@authenticate
def deletePassword(id):
    return delete_password(id)


main()
