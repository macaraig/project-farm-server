from flask import Flask
from flask import jsonify

project_farm_server = Flask(__name__)

@project_farm_server.route("/rainfall")
def get_rainfall():
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
def get_reco():
    recommendations = [
        {
            'id': '1', 
            'cropNameEng': 'Cabbage',
            'cropNameFil': 'Repolyo',
            'link': 'https://hkpinoytv.com/how-to-plant-and-harvest-cabbage/',
            'image': "require('../images/cabbage.jpg')"
        },
        {
            'id': '2', 
            'cropNameEng': 'Garlic',
            'cropNameFil': 'Bawang',
            'link': 'https://hkpinoytv.com/pagtatanim-at-pagluluto-ng-bawang/',
            'image': "require('../images/garlic.jpg')"
        },
        {
            'id': '3', 
            'cropNameEng': 'Eggplant',
            'cropNameFil': 'Talong',
            'link': 'https://hkpinoytv.com/how-to-plant-eggplant/',
            'image': "require('../images/eggplant.jpg')"
        }
    ]
    return jsonify(recommendations)

@project_farm_server.route("/temperature")
def get_temp():
    temp = {
        "Jan" : 25,
        "Feb" : 29,
        "Mar" : 32,
        "Apr" : 40,
        "May" : 29,
        "Jun" : 28,
        "Jul" : 26
    }
    return jsonify(temp)


if __name__ == "__main__":
    project_farm_server.run(debug=True)
