import tkinter as tk
import tkinter.ttk as ttk
from functions import history

# Create the main window
window = tk.Tk()
window.title("Table Example")

# Create the table frame and add it to the main window
table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True)

# Create the table header
header = tk.Label(table_frame, text="History", font=("Arial", 16))
header.pack()

# Create a scrollbar and add it to the table frame
scrollbar = tk.Scrollbar(table_frame)
scrollbar.pack(side="right", fill="y")

# Create a Treeview widget and add it to the table frame
treeview = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set, show="headings")
treeview.pack(side="left", fill="both", expand=True)

# Set the scrollbar to control the Treeview widget
scrollbar.config(command=treeview.yview)

# Create an array of values to display in the table
# values = [["Value 1", "Value 2", "Value 3"],
#           ["Value 4", "Value 5", "Value 6"],
#           ["Value 7", "Value 8", "Value 9"],
#           ["Value 10", "Value 11", "Value 12"]]

values = history("cj@1234")

# Add the column headings to the Treeview widget
treeview["columns"] = ("col1", "col2", "col3","col4")
treeview.column("col1", width=100)
treeview.column("col2", width=100)
treeview.column("col3", width=100)
treeview.column("col4", width=100)
treeview.heading("col1", text="Item")
treeview.heading("col2", text="Total Price")
treeview.heading("col3", text="Units")
treeview.heading("col4", text="Hotel")

# Add the values to the Treeview widget
if values!=None:
    for i, value in enumerate(values):
        treeview.insert("", "end", text="i+1", values=value)

# Run the Tkinter event loop
window.mainloop()