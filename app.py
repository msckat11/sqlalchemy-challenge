######## Imports
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

####### Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

######## Create an app
app = Flask(__name__)

# Define homepage
@app.route("/")
def home():
    return """<h1>Available Routes:</h1>
    <h3>/api/v1.0/precipitation</h3>
    <h3>/api/v1.0/stations</h3>
    <h3>api/v1.0/tobs</h3>
    <h3>/api/v1.0/startdate</h3>
    <h3>/api/v1.0/startdate/enddate</h3>"""

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precip():
    return "<h1>Hawaii Precipitation</h1>"
    session = Session(engine)

    date = dt.datetime(2016, 8, 23)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date).all()

    session.close()

    #turn results into dictionary
    precipitation = []
    for date, precip in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precip"] = precip
        preciptation.append(precip_dict)

    return jsonify(precipitation)

#Stations Route
@app.route("/api/v1.0/stations")
def stations():
    return "<h1>Hawaii Observation Stations</h1>"

# Temperature Route
@app.route("/api/v1.0/tobs")
def temps():
    return "<h1>Hawaii Temperatures</h1>"

if __name__ == "__main__":
    app.run(debug=True)
