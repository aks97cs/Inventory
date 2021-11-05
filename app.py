import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import os

# initialize the window
root = tk.Tk()
root.title("Stock Management System")

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
class WindowTabs:
	def __init__(self, frame_title,
					  entry1_title, 
					  entry2_title, 
					  entry3_title, 
					  entry4_title,
					  tab_name,
					  tab_name_var):

		self.frame_title = frame_title
		self.entry1_title = entry1_title
		self.entry2_title = entry2_title
		self.entry3_title = entry3_title
		self.entry4_title = entry4_title
		self.tab_name = tab_name
		self.tab_name_var = tab_name_var
		# Create the tab bar
		self.tab_bar = ttk.Notebook(root)
		self.tab_bar.pack(expand=1,fill="both")


	def setup_entries(self):
		# Add Inventory Tab
		self.tab_name_var = ttk.Frame(self.tab_bar)
		self.tab_bar.add(self.tab_name_var, text=self.tab_name)
		# Create Item Details Frame inside Inventory tab
		self.item_details_frame = ttk.LabelFrame(self.tab_name_var, text=self.frame_title)
		self.item_details_frame.grid(column=0, row=0, padx=8, pady=4, sticky="N")
		# Product Id label
		self.productId = ttk.Label(self.item_details_frame, text=self.entry1_title)
		self.productId.grid(column=0, row=0, sticky='W')
		# Product Id Entry
		self.productIdEntry = ttk.Entry(self.item_details_frame)
		self.productIdEntry.grid(column=0, row=1, sticky='W')
		# Product Name label
		self.productName = ttk.Label(self.item_details_frame, text=self.entry2_title)
		self.productName.grid(column=0, row=2, sticky='W')
		# Product Name entry
		self.productNameEntry = ttk.Entry(self.item_details_frame)
		self.productNameEntry.grid(column=0, row=3, sticky='W')
		# Product Price label
		self.productPrice = ttk.Label(self.item_details_frame, text=self.entry3_title)
		self.productPrice.grid(column=0, row=4, sticky='W')
		# Product Price entry
		self.productPriceEntry = ttk.Entry(self.item_details_frame)
		self.productPriceEntry.grid(column=0, row=5, sticky='W')
		# Product Quantity label
		self.productQuantity = ttk.Label(self.item_details_frame, text=self.entry4_title)
		self.productQuantity.grid(column=0, row=6, sticky="W")
		# Product Quantity entry
		self.productQuantityEntry = ttk.Entry(self.item_details_frame)
		self.productQuantityEntry.grid(column=0, row=7, sticky="W")
	
	def setup_buttons(self, btn1, btn2, btn3, btn4):
		# Create Insert button
		self.InsertButton = ttk.Button(self.item_details_frame, text=btn1, command=Insert_data)
		self.InsertButton.grid(column=0, row=8, sticky='W', pady=7)
		# Create Show button
		self.ShowButton = ttk.Button(self.item_details_frame, text=btn2, command=Get_data)
		self.ShowButton.grid(column=0, row=8, sticky='E')
		# Create Update button
		self.UpdateButton = ttk.Button(self.item_details_frame, text=btn3, command=Update_data, width=20)
		self.UpdateButton.grid(column=0, row=10, sticky='W')
		# Create Delete button
		self.DeleteButton = ttk.Button(self.item_details_frame, text=btn4, command=Delete_data, width=20)
		self.DeleteButton.grid(column=0, row=11, sticky='W', pady=7)
		# Style the Buttons
		self.style = ttk.Style()
		self.style.configure('TButton', background='#3498db')
		#*************************************************************
	
	def stock_views(self):
		# Create Item Details Frame inside Inventory tab
		self.storage_items = ttk.LabelFrame(self.tab_name_var, text="Product List", borderwidth=3)
		self.storage_items.grid(row=0, column=1, padx=8, pady=4, sticky="N")
		# Create tree/list view
		self.tree = ttk.Treeview(self.storage_items, columns=('Product Id', 'Product Name','Sell Price','Quantity'), height=20)
		self.tree.place(x=30, y=95)
		# Scroll bar for tree
		self.tree_scroll = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
		self.tree_scroll.place(x=30+954+5, y=0, height=200+220)
		self.tree.configure(yscrollcommand=self.tree_scroll.set)
		# Headings for the tree/list
		self.tree.heading('#0', text='Item no.')
		self.tree.heading('#1', text='Product id')
		self.tree.heading('#2', text='Name')
		self.tree.heading('#3', text='Sell Price')
		self.tree.heading('#4', text='Quantity')
		self.tree.column('#1', stretch=tk.YES)
		self.tree.column('#2', stretch=tk.YES)
		self.tree.column('#0', stretch=tk.YES)
		self.tree.column('#3', stretch=tk.YES)
		self.tree.column('#4', stretch=tk.YES)
		self.tree.grid(row=11, columnspan=4, sticky='nsew')
#*************************************************************

inv = WindowTabs('Product Details', 'Product ID: ', 'Product ID: ',
				  'Product ID: ', 'Product ID: ', 'Inventory', 'inventory_tab')
inv.setup_entries()
inv.setup_buttons('insert', 'show', 'update', 'delete')
inv.stock_views()

bill = WindowTabs('Product Details', 'Product ID: ', 'Product ID: ', 
				  'Product ID: ', 'Product ID: ', 'Billing', 'billing_tab')
inv.setup_entries()
inv.setup_buttons('insert', 'show', 'update', 'delete')
inv.stock_views()

root.mainloop()