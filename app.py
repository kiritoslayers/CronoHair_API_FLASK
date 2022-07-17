from flask import Flask
from Entities.contracts import contact

# init flask
app = Flask(__name__)
app.config["DEBUG"] = True

# registrer entitis
app.register_blueprint(contact)


if __name__ == "__main__":
    app.run(debug=True)

