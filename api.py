from flask import Flask, jsonify, make_response, request
import dataset


app = Flask(__name__)
db = dataset.connect('sqlite:///ohio-quarterly.db')

# @app.route('/wells')
# def hello():
#     return 'Hello inerG!'

table = db['OhioWells']

def fetch_db(well_number):  # Each well
    return table.find_one(Well_Number=well_number)

@app.route('/<well_number>', methods=['GET'])
def api_each_well(well_number):
    if request.method == "GET":
        well_obj = fetch_db(well_number)
        if well_obj:
            return make_response(jsonify(well_obj), 200)
        else:
            return make_response(jsonify(well_obj), 404)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)