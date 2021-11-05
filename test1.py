import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import os

# initialize the window
root = tk.Tk()
root.title("Stock Management System")
# Create the tab bar
tab_bar = ttk.Notebook(root)
tab_bar.pack(expand=1,fill="both")
# Add Inventory Tab
inventory_tab = ttk.Frame(tab_bar)
tab_bar.add(inventory_tab, text='Inventory')

# initialize all functions
i=0
def Get_data():
	global i
	global j
	i=0
	tree.delete(*tree.get_children())
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from stock')
	for row in cursor:
		tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3]))
		i=i+1

def Insert_data():
	db = sqlite3.connect('test.db')
	db.execute('insert into stock (Product_Id,Product_Name,Sell_Price,Quantity) values (?,?,?,?)',
				[productIdEntry.get(),
				productNameEntry.get(),
				productPriceEntry.get(),
				productQuantityEntry.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('test.db')
	db.execute('update stock set Product_Id = ? ,Product_Name = ?,Sell_Price = ?,Quantity = ?  where Product_Id = ?',
				(productIdEntry.get(),
				productNameEntry.get(),
				productPriceEntry.get(),
				productQuantityEntry.get(),
				productIdEntry.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('test.db')
	db.execute('delete from stock where Product_Id = ?',(productIdEntry.get(),))
	db.commit()

#*************************************************************
# Create Item Details Frame inside Inventory tab
item_details_frame = ttk.LabelFrame(inventory_tab, text="Item Details")
item_details_frame.grid(column=0, row=0, padx=8, pady=4, sticky="N")
# Product Id label
productId = ttk.Label(item_details_frame, text="Product ID: ")
productId.grid(column=0, row=0, sticky='W')
# Product Id Entry
productIdEntry = ttk.Entry(item_details_frame)
productIdEntry.grid(column=0, row=1, sticky='W')
# Product Name label
productName = ttk.Label(item_details_frame, text="Product Name : ")
productName.grid(column=0, row=2, sticky='W')
# Product Name entry
productNameEntry = ttk.Entry(item_details_frame)
productNameEntry.grid(column=0, row=3, sticky='W')
# Product Price label
productPrice = ttk.Label(item_details_frame, text="Sell Price : ")
productPrice.grid(column=0, row=4, sticky='W')
# Product Price entry
productPriceEntry = ttk.Entry(item_details_frame)
productPriceEntry.grid(column=0, row=5, sticky='W')
# Product Quantity label
productQuantity = ttk.Label(item_details_frame, text="Quantity : ")
productQuantity.grid(column=0, row=6, sticky="W")
# Product Quantity entry
productQuantityEntry = ttk.Entry(item_details_frame)
productQuantityEntry.grid(column=0, row=7, sticky="W")
# Create Insert button
InsertButton = ttk.Button(item_details_frame, text='Insert', command=Insert_data)
InsertButton.grid(column=0, row=8, sticky='W', pady=7)
# Create Show button
ShowButton = ttk.Button(item_details_frame, text='Show', command=Get_data)
ShowButton.grid(column=0, row=8, sticky='E')
# Create Update button
UpdateButton = ttk.Button(item_details_frame, text='Update', command=Update_data, width=20)
UpdateButton.grid(column=0, row=10, sticky='W')
# Create Delete button
DeleteButton = ttk.Button(item_details_frame, text='Delete', command=Delete_data, width=20)
DeleteButton.grid(column=0, row=11, sticky='W', pady=7)
# Style the Buttons
style = ttk.Style()
style.configure('TButton', background='#3498db')
#*************************************************************
# Create Item Details Frame inside Inventory tab
storage_items = ttk.LabelFrame(inventory_tab, text="Product List", borderwidth=3)
storage_items.grid(row=0, column=1, padx=8, pady=4, sticky="N")
# Create tree/list view
tree = ttk.Treeview(storage_items, columns=('Product Id', 'Product Name','Sell Price','Quantity'), height=20)
tree.place(x=30, y=95)
# Scroll bar for tree
tree_scroll = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
tree_scroll.place(x=30+954+5, y=0, height=200+220)
tree.configure(yscrollcommand=tree_scroll.set)
# Headings for the tree/list
tree.heading('#0', text='Item no.')
tree.heading('#1', text='Product id')
tree.heading('#2', text='Name')
tree.heading('#3', text='Sell Price')
tree.heading('#4', text='Quantity')
tree.column('#1', stretch=tk.YES)
tree.column('#2', stretch=tk.YES)
tree.column('#0', stretch=tk.YES)
tree.column('#3', stretch=tk.YES)
tree.column('#4', stretch=tk.YES)
tree.grid(row=11, columnspan=4, sticky='nsew')
#*************************************************************
root.mainloop()