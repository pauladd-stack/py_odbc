import pyodbc
import os
from tkinter import *
from tkinter import ttk
import json
#from dotenv import load_dotenv
#load_dotenv()


CONFIG_FILE = 'config.json'

def save_config(dsn, uid, pwd):
    config = {
        'dsn': dsn,
        'uid': uid,
        'pwd': pwd
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def load_config():
    if os.path.exists(CONFIG_FILE) and os.path.getsize(CONFIG_FILE) > 0:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {'dsn': '', 'uid': '', 'pwd': ''}

def odbc_connect():

    # CONNECTION_STRING="DSN=TestODBC;UID=test;PWD=test"
    #connection_string = os.getenv("CONNECTION_STRING")
    dsn = _dsn.get()
    uid = _uid.get()
    pwd = _pwd.get()
    connection_string = f'DSN={dsn};UID={uid};PWD={pwd}'

    if connection_string is None:
        raise ValueError("No CONNECTION_STRING found in environment variables")
    
    save_config(dsn, uid, pwd)


    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful")
    except pyodbc.Error as e:
        print("Error: ", e)

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM TestTable")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        conn.close()
    except:
        print(connection_string)


root = Tk()
root.title("ODBC_GUI")
frm = ttk.Frame(root, padding=10)
frm.grid(sticky='NSEW')

config = load_config()

ttk.Label(frm, text="DSN:").grid(column=0, row=0, sticky='W')
_dsn = ttk.Entry(frm, width=25)
_dsn.insert(0, config['dsn'])  # Load saved value
_dsn.grid(column=1, row=0, sticky='EW')
ttk.Label(frm, text="UID:").grid(column=0, row=1, sticky='W')
_uid = ttk.Entry(frm, width=25)
_uid.insert(0, config['uid'])  # Load saved value
_uid.grid(column=1, row=1, sticky='EW')
ttk.Label(frm, text="PWD:").grid(column=0, row=2, sticky='W')
_pwd = ttk.Entry(frm, width=25, show='*')
_pwd.insert(0, config['pwd'])  # Load saved value
_pwd.grid(column=1, row=2, sticky='EW')
# Create a button and attach the function to it
ttk.Button(frm, text="Connect", command=odbc_connect).grid(column=1, row=3, columnspan=2, sticky='EW')

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4, columnspan=2, sticky='EW')


# Configure the grid to expand properly
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Ensure the frame expands with the window
frm.grid_columnconfigure(0, weight=1)
frm.grid_columnconfigure(1, weight=3)  # Increase weight for column 1 to make it expand more
frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=1)
frm.grid_rowconfigure(2, weight=1)
frm.grid_rowconfigure(3, weight=1)
frm.grid_rowconfigure(4, weight=1)


root.mainloop()

'''
if __name__ == "__main__":
    main()
'''