from flask import Flask

project_farm_server = Flask(__name__)

rainfall = {
    "Jan" : 3,
    "Feb" : 5,
    "Mar" : 5,
    "Apr" : 6,
    "May" : 7,
    "Jun" : 2,
    "Jul" : 1
}

@project_farm_server.route("/rainfall")
def home():
    return jsonify(rainfall)


if __name__ == "__main__":
    project_farm_server.run(debug=True)
