from flask import Flask
from flask import jsonify

project_farm_server = Flask(__name__)

@project_farm_server.route("/rainfall")
def home():
    rainfall = {
        "Jan" : 3,
        "Feb" : 5,
        "Mar" : 5,
        "Apr" : 6,
        "May" : 7,
        "Jun" : 2,
        "Jul" : 1
    }
    return jsonify(rainfall)

@project_farm_server.route("/recommendations")
def home():
    recommendations = ["rice", "squash", "green chili" ]
    return jsonify(recommendations)


if __name__ == "__main__":
    project_farm_server.run(debug=True)
