#Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, json, jsonify

#Set up Database
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
#reflect the database
Base.prepare(engine, reflect=True)

#references each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database 
session = Session(engine)

#Set Up Flask
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp) .\
        filter(Measurement.date >= prev_year).all()
    precip ={date: prcp for date, prcp in precipitation}
    return jsonify(precip)


    # precipitation = session.query(Measurement.date, Measurement.prcp, func.avg(Measurement.prcp)).\
    #     filter(Measurement.date >= prev_year).\
    #     order_by(Measurement.date).all()
    
    # prcp_data = dict(precipitation)
    # return(prcp_data)


    # precip = {date:prcp for date, prcp in precipitation}
    # return jsonify()
    # # 
    # precipitation = session.query(Measurement.date, Measurement.prcp)
    # filter(Measurement.date >=prev_year).all()
    # precip = {date:prcp for date, prcp in precipitation}
    # return jsonify(precip)