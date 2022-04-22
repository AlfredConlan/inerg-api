import json
from flask import Flask, jsonify, request
import sqlite3

# Set up the app and configure it not to change the order of the json results
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Define the connection and set up error handling in case the connection can't be made
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("ohio-quarterly.db")
    except sqlite3.error as e:
            print(e)
    return conn

###############################################################
# import all the data from the spreadsheet into the database
# create a full crud api and use sql to manipulate data
###############################################################

# Set up the route for the GET request
@app.route("/data", methods=["GET", "POST", "PUT", "DELETE"])
def single_well():
    # Get the arguments passed in - in this case well= and well number
    args = request.args
    well_number = args.get('well')
    quarter = args.get("quarter")
    # Make the connection and set up a cursor for the query
    conn = db_connection()
    cursor = conn.cursor()
    well = None
    if request.method == "GET":
        # Select the record based on the matching well number
        cursor.execute("SELECT * FROM OhioWells WHERE Well_Number=?", (well_number,))
        well = cursor.fetchone()
        # Test that something was returned from the query
        if well is not None:
            # Return the results in the desired format
            newResponse =   {"oil": well[2], "gas":well[3], "brine":well[4]}
            return jsonify(newResponse), 200
        else:
            return jsonify(well), 404
    if request.method == "POST":
        # Select the record based on the matching well number
        cursor.execute("SELECT * FROM OhioWells WHERE Well_Number=?", (well_number,))
        well = cursor.fetchone()
        # Test that something was returned from the query
        if well is not None:
            # Return the results in the desired format
            newResponse =   {"oil": well[2], "gas":well[3], "brine":well[4]}
            return jsonify(newResponse), 200
        else:
            return jsonify(well), 404
    if request.method == "PUT":
        # Select the record based on the matching well number
        cursor.execute("SELECT * FROM OhioWells WHERE Well_Number=?", (well_number,))
        well = cursor.fetchone()
        # Test that something was returned from the query
        if well is not None:
            # Return the results in the desired format
            newResponse =   {"oil": well[2], "gas":well[3], "brine":well[4]}
            return jsonify(newResponse), 200
        else:
            return jsonify(well), 404
    if request.method == "DELETE":
        # Select the record based on the matching well number
        cursor.execute("SELECT * FROM OhioWells WHERE Well_Number=?", (well_number,))
        well = cursor.fetchone()
        # Test that something was returned from the query
        if well is not None:
            # Return the results in the desired format
            newResponse =   {"oil": well[2], "gas":well[3], "brine":well[4]}
            return jsonify(newResponse), 200
        else:
            return jsonify(well), 404

# Set the server to run on localhost port 8080
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=False)
