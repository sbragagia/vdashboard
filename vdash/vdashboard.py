import configparser
import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2 import sql
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Read the config.ini file for login details
config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['database']
dbname = db_config['dbname']
user = db_config['user']
password = db_config['password']
host = db_config['host']
port = db_config['port']

# Establish the database connection

connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
)

cursor = connection.cursor()

# Create the main application window
root = tk.Tk()

# Root window title and dimension
root.title("Formula 1 Championships Data")
root.geometry('600x400')

# Create a custom style for the Treeview widget
style = ttk.Style()
style.configure("Treeview", rowheight=40)

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{x}+{y}')

def fetch_and_display():
    selected_table = table_variable.get()  # Get the selected table from the dropdown

    # Create an SQL Identifier for the selected table name
    table_name_identifier = sql.Identifier(selected_table)

    # Query to fetch column names
    column_query = sql.SQL("SELECT * FROM {} LIMIT 70;").format(table_name_identifier)

    # Execute the query to get column names
    cursor.execute(column_query)
    fetched_names = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Create a new tab for displaying the results
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=selected_table)

    # Create a treeview with columns
    tree = ttk.Treeview(tab, columns=column_names, show='headings', height=80)

    # Set column headings
    for col_name in column_names:
        tree.heading(col_name, text=col_name)
        tree.column(col_name, width=1, anchor='w')

    # Insert rows of data
    for row in fetched_names:
        tree.insert("", "end", values=row)

    # Update column widths based on content
    for col_name in column_names:
        tree.column(col_name, width=tkFont.Font().measure(col_name))
        for row in fetched_names:
            width = tkFont.Font().measure(str(row[column_names.index(col_name)]))
            if width > tree.column(col_name, option="width"):
                tree.column(col_name, width=width)

    # Pack the treeview
    tree.pack(fill="both", expand=True)

    # Create horizontal scrollbar
    xscrollbar = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
    xscrollbar.pack(side="bottom", fill="x")

    # Create vertical scrollbar
    yscrollbar = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
    yscrollbar.pack(side="right", fill="y")

    # Configure treeview to use scrollbars
    tree.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

# Create a variable to store the selected table name
table_variable = tk.StringVar()

# Create a label for the table selection
table_label = tk.Label(root, text="Select a Table:")
table_label.pack()

# Create a dropdown menu (combobox) for table selection
table_dropdown = ttk.Combobox(root, textvariable=table_variable)
table_dropdown['values'] = (
    'circuits', 'constructor_results', 'constructors', 'constructor_standings', 'drivers', 'driver_standings', 'lap_times', 'pit_stops', 'qualifying', 'races', 'results', 'seasons', 'sprint_results', 'status'
)
table_dropdown.pack()

# Set a predefined selection
table_variable.set('drivers')

# Create a button to fetch column names and display the data in a Treeview
fetch_button = tk.Button(root, text="Fetch Columns and Data", command=fetch_and_display)
fetch_button.pack()

# Create a notebook (tabbed interface) to display the results
notebook = ttk.Notebook(root)
notebook.pack()

# Center the window on the screen
root.update()  # Make sure the window has been fully initialized before centering it
center_window(root, 800, 600)  # Adjust the size as needed

# Load a Formula 1 car image
car_image = Image.open('formula1_car.png')
car_image = car_image.resize((400, 200), Image.LANCZOS)  # Resize the image
car_photo = ImageTk.PhotoImage(car_image)

# Create a label to display the car image in the bottom right
car_label = tk.Label(root, image=car_photo)
car_label.photo = car_photo  # Store a reference to avoid garbage collection
car_label.pack(side="bottom", anchor="se", padx=10, pady=10)  # Adjust the padding as needed

# Start the Tkinter main loop
root.mainloop()

# Close the connection when the application is closed
connection.close()
