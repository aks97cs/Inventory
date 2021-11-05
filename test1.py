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
# Add Inventory Tab
inventory_tab = ttk.Frame(tab_bar)
tab_bar.add(inventory_tab,text='Inventory')
# Create Item Details Frame inside Inventory tab
item_details_frame = ttk.LabelFrame(inventory_tab,text="Item Details")
item_details_frame.grid(column=0,row=0,padx=8,pady=4,sticky="N")
# Fill t
global PRODUCT_QUANTITY_VALUE
# global PRODUCT_ID_VALUE
global PRODUCT_PRICE_VALUE
global PRODUCT_NAME_VALUE

# PRODUCT_ID_VALUE = tk.StringVar()
PRODUCT_NAME_VALUE = tk.StringVar()
PRODUCT_PRICE_VALUE = tk.StringVar()
PRODUCT_QUANTITY_VALUE = tk.StringVar()

productId = ttk.Label(item_details_frame,text="Product ID: ")
productIdEntry = ttk.Entry(item_details_frame)
productIdEntry.grid(column=0,row=1,sticky='W')
productName = ttk.Label(item_details_frame,text="Product Name : ")
#productName.config(font=("Courier",15))
productNameEntry = ttk.Entry(item_details_frame,textvariable=PRODUCT_NAME_VALUE)
#productNameEntry.config(font=("Courier",20))
productPrice = ttk.Label(item_details_frame,text="Sell Price : ")
#productPrice.config(font=("Courier",15))
productPriceEntry = ttk.Entry(item_details_frame,textvariable=PRODUCT_PRICE_VALUE)
#productPriceEntry.config(font=("Courier",20))
productPriceEntry.grid(column=0,row=5,sticky='W')
productQuantity = ttk.Label(item_details_frame,text="Quantity : ")
#productQuantity.config(font=("Courier",15))
productQuantityEntry = ttk.Entry(item_details_frame,textvariable=PRODUCT_QUANTITY_VALUE)
#productQuantityEntry.config(font=("Courier",20))
productQuantityEntry.grid(column=0,row=7,sticky="W")
#*************************************************************



labelFrame1 = ttk.LabelFrame(inventory_tab,text="Product List",borderwidth=3)
labelFrame1.grid(row=0,column=1,padx=8,pady=4,sticky="N")




#******************************** Get DATA *******************************
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
	db.execute('insert into stock (Product_Id,Product_Name,Sell_Price,Quantity) values (?,?,?,?)',[productIdEntry.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('test.db')
	db.execute('update stock set Product_Id = ? ,Product_Name = ?,Sell_Price = ?,Quantity = ?  where Product_Id = ?',(productIdEntry.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(),productIdEntry.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('test.db')
	db.execute('delete from stock where Product_Id = ?',(productIdEntry.get(),))
	db.commit()


#************************************ TREE VIEW *******************************************

tree = ttk.Treeview(labelFrame1, columns=('Product Id', 'Product Name','Sell Price','Quantity'),height=20)
tree.place(x=30, y=95)
vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
vsb.place(x=30+954+5, y=0, height=200+220)

tree.configure(yscrollcommand=vsb.set)
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





InsertButton = ttk.Button(item_details_frame,text='Insert',command=Insert_data)
ShowButton = ttk.Button(item_details_frame,text='Show',command=Get_data)



style = ttk.Style()
style.configure('TButton', background='#3498db')


UpdateButton = ttk.Button(item_details_frame,text='Update',command=Update_data,width=20)
DeleteButton = ttk.Button(item_details_frame,text='Delete',command=Delete_data,width=20)
DeleteButton.grid(column=0,row=11,sticky='W',pady=7)
UpdateButton.grid(column=0,row=10,sticky='W')
ShowButton.grid(column=0,row=8,sticky='E')
InsertButton.grid(column=0,row=8,sticky='W',pady=7)
productQuantity.grid(column=0,row=6,sticky="W")
productPrice.grid(column=0,row=4,sticky='W')
productNameEntry.grid(column=0,row=3,sticky='W')
productName.grid(column=0,row=2,sticky='W')
productId.grid(column=0,row=0,sticky='W')

tab_bar.pack(expand=1,fill="both")


#****************************************************************

tab2 = ttk.Frame(tab_bar)
tab_bar.pack(expand=1,fill="both")

root.mainloop()