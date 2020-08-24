# Import Flask
from flask import Flask

# Create an app
app = Flask(__name__)

#Define homepage
@app.route("/")
def home():
    return "Available Routes:    /api/v1.0/precipitation    /api/v1.0/stations      /api/v1.0/tobs      /api/v1.0/<start>       /api/v1.0/<start>/<end>"

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precip():
    return "Hawaii Precipitation"

#Stations Route
@app.route("/api/v1.0/stations")
def stations():
    return "Hawaii Observation Stations"

# Temperature Route
@app.route("/api/v1.0/tobs")
def temps():
    return "Hawaii Temperatures"

if __name__ == "__main__":
    app.run(debug=True)
