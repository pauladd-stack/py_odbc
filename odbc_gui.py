from tkinter import *
from tkinter import ttk, Label, StringVar
from odbc import odbc_class
from config import load_config
from dotenv import load_dotenv
load_dotenv()

config = load_config()
        
def fill_tree(rows)-> None:
    for item in tree.get_children():
            tree.delete(item)

    for row in rows:
        tree.insert('', 'end', values=row)

def update_label(text)-> None:
    wrapped_text = wrap_text(text, 200)  # Adjust the width for wrapping
    status_text.set(wrapped_text)

def wrap_text(text, width)-> str:
    return '\n'.join(text[i:i+width] for i in range(0, len(text), width))

def connect_and_update(dsn, uid, pwd, table)-> None:
    db = odbc_class(dsn, uid, pwd, table)    
    label, rows = db.execute()
    del db
    update_label(label)
    fill_tree(rows)





root = Tk()
root.title("ODBC_GUI")
root.geometry("600x400")
frm = ttk.Frame(root, padding=10)
frm.grid(sticky='NSEW')

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

ttk.Label(frm, text="Table:").grid(column=0, row=3, sticky='W')
_table = ttk.Entry(frm, width=25)
_table.insert(0, config['table'])  # Load saved value
_table.grid(column=1, row=3, sticky='EW')

# Create a Treeview widget
tree = ttk.Treeview(frm, columns=('col1', 'col2', 'col3'), show='headings')
tree.heading('col1', text='Column 1')
tree.heading('col2', text='Column 2')
tree.heading('col3', text='Column 3')
tree.grid(column=0, row=4, columnspan=2, sticky='NSEW')

# Configure column widths (optional)
tree.column('col1', width=100)
tree.column('col2', width=100)
tree.column('col3', width=100)

# Create a label to display status messages
status_text = StringVar()
status_label = Label(frm, textvariable=status_text, wraplength=400, justify="left")
status_label.grid(column=0, row=5, rowspan=2, sticky='W')
# Create a button and attach the function to it
ttk.Button(frm, text="Connect", command=lambda: connect_and_update(_dsn.get(), _uid.get(), _pwd.get(), _table.get())).grid(column=1, row=5, columnspan=1, sticky='EW')

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6, columnspan=1, sticky='EW')


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
frm.grid_rowconfigure(4, weight=3)  # Increase weight for row 3 to allow Treeview to expand
frm.grid_rowconfigure(5, weight=1)
frm.grid_rowconfigure(6, weight=1)


root.mainloop()

'''
if __name__ == "__main__":
    main()
'''