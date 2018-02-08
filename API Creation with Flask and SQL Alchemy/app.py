# @TODO: Import Dependencies Here
from flask import Flask, jsonify, g
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlalchemy
import numpy as np
#################################################
# Database Setup
#################################################
# @TODO: YOUR CODE HERE
dialect = 'sqlite'
port = 3306
database = 'hawaii.sqlite'

engine = create_engine(f'{dialect}:///{database}')
# reflect an existing database into a new model
# @TODO: YOUR CODE HERE
Base = automap_base()
Base.prepare(engine, reflect=True)

print(Base.classes.keys())
# reflect the tables
# @TODO: YOUR CODE HERE

# Save references to the invoices and invoice_items tables
# @TODO: YOUR CODE HERE

# Create our session (link) from Python to the DB
# @TODO: YOUR CODE HERE
session = Session(bind=engine)
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
# @TODO: YOUR CODE HERE

app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# @TODO Uncomment the following and complete the code for
# all of the routes listed using queries from part1 of this assignment.
@app.route("/api/v1.0/")
def home():
    return(
        f"Available  Routes:</br>"
        f"/api/v1.0/precipitation: Query for the dates and temperature observations from the last year.<br/>"
        f"/api/v1.0/stations: Return a list of stations from the dataset.<br/>"
        f"/api/v1.0/tobs: Return a list of Temperature Observations for the previous year<br/>"
        f"/api/v1.0/start and /api/v1.0/start/end: Return a list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>"
        )
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_year = session.query(Measurement).filter(Measurement.date >= '2016-08-23').filter(Measurement.date <='2017-08-23')
    results = []
    for rows in last_year:
        results_dict = {}
        results_dict['date'] = rows.date
        results_dict['prcp'] = rows.prcp
        results.append(results_dict)
    return jsonify(results)


@app.route("/api/v1.0/stations")
def active_stations():
    active_stations = session.query(Station).all()
    act_stat = []
    for row in active_stations:
        act_stat_dict = {}
        act_stat_dict['station'] = row.station
        act_stat.append(act_stat_dict)
    return jsonify(act_stat)

@app.route("/api/v1.0/tobs")
def stations_tobs():
    station_tobs = []
    for row in last_year:
        station_dict = {}
        station_dict['station'] = rows.station
        station_dict['tobs'] = rows.tobs
        station_tobs.append(station_dict)
    return jsonify(station_tobs)

@app.route("/api/v1.0/<start>")
def start_query(start):
    start_q = session.query(Measurement.date, func.min(Measurement.tobs).label("Temp Min"),func.max(Measurement.tobs).label("Temp Max"),func.avg(Measurement.tobs).label("Temp Max"))\
    .filter(Measurement.date >= start).group_by(Measurement.date).all()
    start_ravel = list(np.ravel(start_q))
    start_list = []
    for row in start_q:
        test_dict = {}
        test_dict['Temps (Min, Max, Average)'] = row
        start_list.append(test_dict)
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_query(start,end):
    start_end_q = session.query(Measurement.date, func.min(Measurement.tobs).label("Temp Min"),func.max(Measurement.tobs).label("Temp Max"),func.avg(Measurement.tobs).label("Temp Max"))\
    .filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    start_end_ravel = list(np.ravel(start_end_q))
    start_end_list = []
    for row in start_end_q:
        test_dict = {}
        test_dict['Temps (Min, Max, Average)'] = row
        start_end_list.append(test_dict)
    return jsonify(start_end_list)

if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE
    app.run(debug=True)
    raise NotImplementedError()