# Data Visualization Dashboard

Data visualization dashboard with the purpose of demonstrating programming skills, in particular Python and SQL.
It currently displays a Tkinter window that connects to a remote PostgreSQL server, with the possibility of choosing one option out of 14 tables, and displays the data.

The data is taken from the "Formula 1 Championships" dataset from kaggle.com

# How to use
Download the /vdash/ folder, edit the config.ini file with the password and run vdashboard.py  
`python3 vdashboard.py`

# Requirements
The required libraries are psycopg2 and Pillow  
`pip install psycopg2`  
`pip install pillow`

What has been done so far:
# Database Initialization
- Downloaded the dataset from Kaggle, with the 14 .csv files
- Created a database
- Created a user on PostgreSQL and granted privileges and ownership for the schema and database
- Created the 14 tables with the columns and datatypes on pg Admin 4
- Imported the 14 .csv files in the tables with a bash shell .sh script, through a "COPY FORM" cycle
- Realized a ERD.pgerd graphical display of the database, implementing foreign keys and relations appropriately
- Loaded the database on a privately hosted PostgreSQL database for remote access

# Visualization Dashboard
- Using Tkinter and the psycopg2 library, wrote a .py script that opens a window and allows the user to choose one of the 14 tables and display the data
- It incorporates PSQL remote connections and simple queries
- Displays the data in a treeView
- Stylized the window through proper labeling
- The cells of the treeview have a dynamic width
- Added a small graphical image for flavor

# What's next
- Adding graphs through the Matplotlib, Seaborn, and Plotly libraries
- Adding more queries, with right click and mouseover options to explore the data
- Feedback and testing
- Improving the security of the remote accessing methods
