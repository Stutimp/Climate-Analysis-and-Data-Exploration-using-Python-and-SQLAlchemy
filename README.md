# SQLAlchemy-Challenge
## Module 10 Challenge
## Introduction

I used the **Python and SQLAlchemy for this assignment to do a basic climate analysis and data exploration of the provided climate database**. I mainly used SQLAlchemy ORM queries, Pandas, and Matplotlib for this particular data analysis. Which started with importing all the required dependencies. The assignment mainly has the following sections:
 ###  Precipitation Analysis:
 First, I found the most recent data in the dataset, and using that date, I got the previous 12 months of precipitation data by querying the previous 12 months of data. Finally, Using the Pandas, I Plotted the results with Matplotlib to plot the data.
  
 ### Exploratory Station Analysis:
   For this, I queried out the total number of the stations in the dataset and also found the most-active stations (the stations with the most rows). After that, I designed a query that calculates the lowest, highest, and average temperatures that filter on the most active station ID found in the previous query.
   I also queried to get the previous 12 months of temperature observation (TOBS) data and finally plotted the results as a histogram.
###  Designing the Climate App:
Based on the queries and analysis I made in the jupyter notebook, I designed a **Flask API** in the following ways:
- I started with the homepage, where I listed all the **available routes** like the following:
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f" Dynamic Route: /api/v1.0/&lt;start&gt;<br/>"
        f"Dynamic Route: /api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
- For each route, I defined a separate function that would run the respective code blocks, which would eventually be browsable when a user hits the respective links. 
- I also made the last two links that would open the browsers with the JSONified list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
- I used the Flask JSONify function to convert the API data to a valid JSON response object.

During this assignment, I received support from my resourceful boot camp tutor and some LAs, which helped me complete my assignment.

Thank you!
