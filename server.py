from flask import Flask

project_farm_server = Flask(__name__)

@project_farm_server.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    project_farm_server.run(debug=True)
