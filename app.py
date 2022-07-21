from flask import Flask
from Entities.contact import contact

# init flask
app = Flask(__name__)
app.config["DEBUG"] = True

# registrer entities
app.register_blueprint(contact)

# init this application
if __name__ == "__main__":
    app.run(debug=True)

