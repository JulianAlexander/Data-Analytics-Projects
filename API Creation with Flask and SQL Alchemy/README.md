Using Python, Flask, and SQL Alchemy, I've created an API containing temperature and preciptation data from Honolulu, Hawaii. 

Step 1 - Data Engineering
The climate data for Hawaii is provided through two CSV files. The data was inspected and cleaned using Python. 
Data_engineering.ipynb contains the completed code. The cleaned csv files were saved with a "clean_" prefix.

Step 2 - Database Engineering
With the cleaned data in the clean_ .csv files, thanks to SQLAlchemy and it's declarative_base function, the table schemas were modeled ( ORM classes were created for Measurements and for stations) and a sqlite database created (hawaii.sqlite). 
Database_engineering.ipynb contains the completed code. 

Step 3 - Climate Analysis and Exploration
The previous 2 steps now allow for basic climate analysis and data exploration of the new weather station tables. 
All of the following analysis was completed using SQLAlchemy ORM queries (create_engine, automap_base), Pandas, and Matplotlib using a two week vacation period with arbitrary start dates.

Feedback is always appreciated! Thanks
