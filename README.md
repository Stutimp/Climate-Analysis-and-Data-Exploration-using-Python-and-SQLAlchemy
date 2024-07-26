# Climate Analysis and Data Exploration using Pyhton and SQLAlchemy

## Project Overview
This project involves conducting a basic climate analysis and data exploration of a provided climate database using Python and SQLAlchemy. The project is divided into two main parts:

1. Climate Data Analysis
2. Designing a Climate Flask API

## Part 1: Climate Data Analysis

### Objective
To perform a basic climate analysis and data exploration of the provided climate database using Python, SQLAlchemy, Pandas, and Matplotlib.

**Steps Taken**

I used the **Python and SQLAlchemy for this assignment to do a basic climate analysis and data exploration of the provided climate database**. I mainly used SQLAlchemy ORM queries, Pandas, and Matplotlib for this particular data analysis. Which started with importing all the required dependencies. The assignment mainly has the following sections:

1. Precipitation Analysis
- **Found the Most Recent Date:** Identified the most recent date in the dataset.
- **Retrieve Precipitation Data:** Queried the previous 12 months of precipitation data.
- **Load Data into DataFrame:** Loaded the query results into a Pandas DataFrame, sorted by date.
- **Plot Results:** Visualized the precipitation data using Matplotlib.
-**Summary Statistics:** Printed summary statistics for the precipitation data.

2. **Exploratory Station Analysis**
- **Total Number of Stations:** Queried the total number of stations in the dataset.
- ***Most Active Stations:** Identified the stations with the most observations.
- **Temperature Analysis for Most Active Station:** Queried the lowest, highest, and average temperatures for the most active station.
- **Temperature Observations:** Retrieved the previous 12 months of temperature observation data and plotted as a histogram.

### Findings
Detailed explanations are provided for each plot, describing noticeable trends and relationships.

## Part 2: Designing the Climate Flask API

### Objective
To design a Flask API based on the queries developed in the Jupyter notebook, providing various routes to access climate data.

**Steps Taken**
**Routes Created**
- **Homepage (/):** Lists all available routes like the following:
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f" Dynamic Route: /api/v1.0/&lt;start&gt;<br/>"
        f"Dynamic Route: /api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"

- **Precipitation Route (/api/v1.0/precipitation):** Returns JSON representation of the last 12 months of precipitation data.
- **Stations Route (/api/v1.0/stations):** Returns a JSON list of all stations in the dataset.
- **Temperature Observations Route (/api/v1.0/tobs):** Returns a JSON list of temperature observations for the previous year for the most active station.
- **Start Route (/api/v1.0/<start>):** Returns a JSON list of the minimum, average, and maximum temperatures from the start date to the end of the dataset.
- **Start/End Route (/api/v1.0/<start>/<end>):** Returns a JSON list of the minimum, average, and maximum temperatures for the specified date range.

For each route, I defined a separate function that would run the respective code blocks, which would eventually open a browser when a user hits the respective links. 
- I also made the last two links dynamic that would take the user input for the start date and end date within the dataset and would open the browsers with the JSONified list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
- I used the Flask JSONify function to convert the API data to a valid JSON response object.

### Tools & Techniques

- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask

### Applications

- **Precipitation Analysis:** Provides insights into precipitation trends and patterns over a 12-month period.
- **Exploratory Station Analysis:** Identifies active weather stations and analyzes temperature trends.
- **Dynamic Climate Data API:** Offers dynamic querying of climate data based on user-defined date ranges, useful for detailed climate analysis.

## Conclusion
This project demonstrates the use of Python, SQLAlchemy, Pandas, Matplotlib, and Flask to conduct climate data analysis and create a dynamic API for accessing climate data. The insights gained can benefit various applications, from climate research to tourism planning.


Thank you!
