import json
from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("ohio-quarterly.db")
    except sqlite3.error as e:
            print(e)
    return conn

@app.route("/data", methods=["GET"])
def single_well():
    args = request.args
    well_number = args.get('well')
    conn = db_connection()
    cursor = conn.cursor()
    well = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM OhioWells WHERE Well_Number=?", (well_number,))
        well = cursor.fetchone()
        if well is not None:
            newResponse =  {"oil": well[2], "gas":well[3], "brine":well[4]}
            return jsonify(newResponse), 200
        else:
            return jsonify(well), 404

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
