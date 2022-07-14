from flask import Flask
from flask import blueprints
import psycopg2
from usuario import usuario

# a parte de conexão com o banco de dados
POSTGRESQL_URI = "postgres://lvwcicxncrwxcg:9ccbcf890a4cbaae505e0864590aab79606bf4aff835d140cc9a062ab3dde74e@ec2-18-204-142-254.compute-1.amazonaws.com:5432/d79r2kcmsirp15"
connection = psycopg2.connect(POSTGRESQL_URI)

# Instanceando o flask 
app = Flask(__name__)
# registrando as entidades
app.register_blueprint(usuario.usuario)

