#Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract

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
    Welcome to the Hawaii Temperature Analysis API!</br>
    <font color=blue>Available Routes:</font></br>
    /api/v1.0/June</br>
    /api/v1.0/December</br>
    ''')

@app.route("/api/v1.0/June")
def June_temperatures():
    print("\n======================")
    print("June_temperature")
    print("======================\n")

    session = Session(engine)

    temps = session.query(Measurement).filter(extract('year',Measurement.date) ==2017).\
        filter(extract('month',Measurement.date) ==6)

    # print("\n======================")
    # print(f"temps= {temperature}")
    # print("======================\n")

    # June_Temps = []
    # temp_df = pd.DataFrame()

    # for date, temp in temperature:
    #     # 
    #     # print(f"date={date} temp={temp}")
    #     temp_df[date] = temp
   
    # # temps =  list(np.ravel(temperature))   

    # print("\n======================")
    # print(f"This your June tempertures= {temp_df}")
    # print("======================\n")

    temp_list = []
    temp_df = {}
    for temp in temps:
        # print(f"{date}  {temp}")
        # temp_df["date"] = temp.date
        # temp_df["temp"] = temp.tobs
        # temp_list.append(temp_df)
        # break
        temp_list.append([temp.date, temp.tobs])
 
    # temp_list
        
    session.close
    return jsonify(June_temperatures=temp_list)

@app.route("/api/v1.0/December")
def Decemeber_temperatures():
    print("\n======================")
    print("Dec_temperature")
    print("======================\n")

    session = Session(engine)

    temperature = session.query(Measurement).filter(extract('year',Measurement.date) ==2017).\
        filter(extract('month',Measurement.date) ==12)

    # print("\n======================")
    # print(f"temps= {temperature}")
    # print("======================\n")
    
    # Dec_Temps = []
    # temp_df = pd.DataFrame()

    # for date, temp in temperature:
    #     # 
    #     # print(f"date={date} temp={temp}")
    #     temp_df[date] = temp
   
    temps =  list(np.ravel(temperature))   

    # print("\n======================")
    # print(f"This your June tempertures= {temp_df}")
    # print("======================\n")

    temp_list = []
    temp_df = {}
    for temp in temps:
        # print(f"{date}  {temp}")
        # temp_df["date"] = temp.date
        # temp_df["temp"] = temp.tobs
        # temp_list.append(temp_df)
        # break
        temp_list.append([temp.date, temp.tobs])
 
   
        
    session.close
    return jsonify(Dec_temps=temp_list)
    