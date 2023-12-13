# Importing the dependencies.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from datetime import datetime, timedelta
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
hawaii_stations = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

  
   # Creating route for home page
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f" Dynamic Route: /api/v1.0/&lt;start&gt;<br/>"
        f"Dynamic Route: /api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )
      
#########################################################
   # Creating route for precipitation   
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Creating our session (link) from Python to the DB
    session = Session(engine)

   # Finding the most recent date in the database and putting that value to find the "one_year_ago" date using syntax, one_year_ago = most_recent_date - timedelta(days=365)
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d').date()
    # Calculating one year ago from the most recent date
    one_year_ago= dt.date(2017,8,23) - dt.timedelta(days=365)
  
    # Performing a query to retrieve the data and precipitation scores retrieving only the last 12 months of data
    precipitation_data = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= one_year_ago).all()

    # Converting the query results to a dictionary using date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    # Closing the session before returning the data
    session.close()

    return jsonify(precipitation_dict)    
    
   ##############################################################
  
   # Creating route for stations  

@app.route("/api/v1.0/stations")
def stations():
    # Create a database session
    session = Session(engine)
   
    # Querying and returning a JSON list of stations from the dataset

    station_data = session.query(hawaii_stations.station, hawaii_stations.name).all()
    #station_data 
    station_pair = {station : name for station, name in station_data}
    station_pair   
  
    
    # Closing the session before returning the data
    session.close()

    return jsonify(station_pair )    
    
  ##################################################################

   # Creating route for Temprature Observations (TOBS)
@app.route("/api/v1.0/tobs") 
def temp_obser():
    # Create a database session
    session = Session(engine)
   
    # Querying and returning  the dates and temperature observations of the most-active station for the previous year of data and JSONfying it.

    """Quering the dates and temperature observations of the most-active station, which is 'USC00519281' as per our jupyter notebook analysis, for the previous year of data"""
    most_active_station_id = 'USC00519281'
    session = Session(engine)
    temprature_data = session.query(measurement.date,measurement.tobs).filter(measurement.station == most_active_station_id).\
    order_by(measurement.date.desc()).limit(365).all()
    temprature_data
    #Using list comprehension 
    most_active_stations_list = [(temprature[0],temprature[1]) for temprature in temprature_data]
    most_active_stations_list
    
    # Closing the session before returning the data
    session.close()

    return jsonify(most_active_stations_list)    

################################################################
 # Creating  route for a specified start 
@app.route('/api/v1.0/<start>',methods=['GET'])
def start_route(start):

    # Create a database session
    session = Session(engine)

    """ Returning temperature data from the start date onwards """

    #Taking the single maximum and latest date in the measurement table  and defining the start_date  as datetime objects
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d').date()
    start_date = datetime.strptime(f'{start}','%Y-%m-%d').date()
    
    #Quering the temprature for the last 12 months and get thee minimum, maximum and average tempratures from start date to most recent date
    temp_starts_date = session.query(
    func.min(measurement.tobs).label('min_temp'),
    func.avg(measurement.tobs).label('avg_temp'),
    func.max(measurement.tobs).label('max_temp')
).filter(measurement.date >= start_date, measurement.date <= most_recent_date).all()

    #extracting the tempratire stats from the query result and JSONifying it
    temprature_dict_data = {
        'min_temp': temp_starts_date[0].min_temp,
        'avg_temp': temp_starts_date[0].avg_temp,
        'max_temp': temp_starts_date[0].max_temp
    }

     # Closing the session before returning the data
    session.close()

    return jsonify(temprature_dict_data)
###########################################################
# Creating route for a start-end range
@app.route('/api/v1.0/<start>/<end>',methods = ['GET'])
def start_end_date_data(start,end):

    # Create a database session
    session = Session(engine)
   
   #defining the start_date and end_date as datetime objects

    start_date = datetime.strptime(start,'%Y-%m-%d').date()
    end_date = datetime.strptime(end,'%Y-%m-%d').date()

#Quering the temprature for the last 12 months and get thee minimum, maximum and average tempratures from start date to most recent date

    temp_starts_end = session.query(
    func.min(measurement.tobs).label('min_temp'),
    func.avg(measurement.tobs).label('avg_temp'),
    func.max(measurement.tobs).label('max_temp')
).filter(measurement.date >= start_date, measurement.date <= end_date).all()

    #extracting the tempratire stats from the query result and JSONifying it
    temprature_start_end_dict = {
        'min_temp': temp_starts_end[0].min_temp,
        'avg_temp': temp_starts_end[0].avg_temp,
        'max_temp': temp_starts_end[0].max_temp
    }

     # Closing the session before returning the data
    session.close()

    return jsonify(temprature_start_end_dict)



if __name__ == '__main__':
    app.run(debug=True)
