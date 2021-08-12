#Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

