# Import Flask
from flask import Flask

# Create an app
app = Flask(__name__)

#Define homepage
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
