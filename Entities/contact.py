from flask import Blueprint, jsonify
from Helpers import helpers


contact = Blueprint('contact', __name__)

@contact.route('/api/v1/account/contact', methods=["GET"])
def GetAlllContacts():
    try:
        database = helpers.GetConnectionString()
        cur = database.cursor()
        sql = """select * from "cronoHair".contato c;"""
        cur.execute(sql)
        database.commit()
        dados = cur.fetchall()
        cur.close()
        return jsonify(dados)
    except:
        return "Error"


@contact.route('/api/v1/account/contact', methods=["GET"])
def GetById(id):
    try:
        database = helpers.GetConnectionString()
        cur = database.cursor()
        sql = f"""select * from "cronoHair".contato c where id = {id};"""
        cur.execute(sql)
        database.commit()
        dados = cur.fetchall()
        cur.close()
        return jsonify(dados)
    except:
        return "Error"