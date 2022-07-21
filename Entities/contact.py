import json
from flask import Blueprint, jsonify
from Helpers import helpers

# create routes blueprint
contact = Blueprint('contact', __name__)

# declare route
@contact.route('/api/v1/customer/', methods=["GET"])
def GetAllContacts():
    try:
        # Get connection with heroku
        database = helpers.GetConnection()
        # cursor for consult
        cur = database.cursor()
        sql = """select * from "cronoHair".contato c;"""
        # execute sql
        cur.execute(sql)
        # return consult database
        dice = cur.fetchall()
        # close connection with database
        cur.close()
        # create list for return in json
        list = []
        for dices in dice:
            # create json for return
            dict = {
                "id": dices[0],
                "nome": dices[1],
                "telefone": dices[2],
                "telefone 2": dices[3]
            }
            # add json in list
            list.append(dict)
        # return list json
        return json.dumps(list)
    except Exception:
        return Exception


# declare route with parametres Id
@contact.route('/api/v1/customer/<int:id>', methods=['POST', 'GET'])
def GetById(id):
    try:
        # open connection with database
        database = helpers.GetConnection()
        # cursor for consult
        cur = database.cursor()
        sql = f"""select * from "cronoHair".contato c where id = {id};"""
        # execute a query in sql
        cur.execute(sql)
        # return consult database
        dice = cur.fetchall()
        # close database connection
        cur.close()
        # return one dice in json
        dict = {
            "id": dice[0][0],
            "nome": dice[0][1],
            "telefone": dice[0][2],
            "telefone 2": dice[0][3]
        }
        # return one dice in json
        return jsonify(dict)
    except Exception:
        return Exception


# stop here. I go search how can make this!
@contact.route('/api/v1/customer/<int:id>', methods=['POST'])
def CreateCustomer():
    pass


