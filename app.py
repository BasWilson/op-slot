from tables import create_passwords_table
from flask import Flask
from flask import request
from httpHelpers import stringToJsonError
from dbHelpers import create_connection, create_table, create_password, get_passwords, delete_password, update_password

app = Flask(__name__)


def main():
    create_table(create_passwords_table)


@app.route('/passwords', methods=['GET'])
def getPasswords():
    return get_passwords("test")


@app.route('/passwords', methods=['POST'])
def createPassword():
    return create_password(("test", request.json['username'], request.json['password']))


@app.route('/passwords', methods=['PUT'])
def updatePassword():
    return update_password(request.json['username'], request.json['password'], request.json['id'], "test")


@app.route('/passwords/<id>', methods=['DELETE'])
def deletePassword(id):
    return delete_password(id)


main()
