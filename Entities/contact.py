import json
from flask import Blueprint, jsonify
from Helpers import helpers


contact = Blueprint('contact', __name__)


@contact.route('/api/v1/customer/', methods=["GET"])
def GetAllContacts():
    try:
        database = helpers.GetConnectionString()
        cur = database.cursor()
        sql = """select * from "cronoHair".contato c;"""
        cur.execute(sql)
        database.commit()
        dados = cur.fetchall()
        cur.close()
        list = []
        for dado in dados:
            print(dado)
            dict = {
                "id": dado[0],
                "nome": dado[1],
                "telefone": dado[2],
                "telefone 2": dado[3]
            }
            list.append(dict)
        
        return json.dumps(list)
    except:
        return "Erro"


@contact.route('/api/v1/customer/<int:id>', methods=['POST', 'GET'])
def GetById(id):
    try:
        database = helpers.GetConnectionString()
        cur = database.cursor()
        sql = f"""select * from "cronoHair".contato c where id = {id};"""
        cur.execute(sql)
        database.commit()
        dados = cur.fetchall()
        dict = {
            "id": dados[0][0],
            "nome": dados[0][1],
            "telefone": dados[0][2],
            "telefone 2": dados[0][3]

        }
        cur.close()
        return jsonify(dict)
    except:
        return "Error"
