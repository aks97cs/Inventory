import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
root = tk.Tk()
root.title("Stock Management System")
tabcontrol = ttk.Notebook(root)
Inventory = ttk.Frame(tabcontrol)
labelFrame = ttk.LabelFrame(Inventory,text="Inventory Management")
labelFrame.grid(column=0,row=0,padx=8,pady=4,sticky="N")


#*************************************************************



tabcontrol1 = ttk.Notebook(root)
Inventory1 = ttk.Frame(tabcontrol1)

labelFrame1 = ttk.LabelFrame(Inventory,text="Product List",borderwidth=3)
#labelFrame1.grid_propagate(0)
labelFrame1.grid(row=0,column=1,padx=8,pady=4,sticky="N")

Inventory1.pack()
PRODUCT_ID = ttk.Label(labelFrame1,text="PRODUCT_ID :",width=20)
PRODUCT_ID.config(font=("Courier",15))
PRODUCT_ID.grid(column=0,row=0)
PRODUCT_NAME = ttk.Label(labelFrame1,text="PRODUCT_NAME :",width=22)
PRODUCT_NAME.config(font=("Courier",15))
PRODUCT_NAME.grid(column=1,row=0)
SELL_PRICE = ttk.Label(labelFrame1,text="SELL_PRICE : ",width=12)
SELL_PRICE.config(font=("Courier",15))
style=ttk.Style()
SELL_PRICE.configure(style="Label")
style.configure("Label", foreground="red")
SELL_PRICE.grid(column=2,row=0)

#******************************** Get DATA *******************************

def Get_data():
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from test')
	for row in cursor:
		src.insert(1.0,row[0])
		src.insert(1.0,row[1])
		src.insert(1.0,row[2])

def Insert_data():
	db = sqlite3.connect('test.db')
	cursor = db.execute()



k='BoomShiva'	
src = scrolledtext.ScrolledText(labelFrame1,width=104,height=30,wrap=tk.WORD)
src.insert(1.0,k)
src.grid(column=0,columnspan=4,row=12,sticky=tk.W)
#tabcontrol1.add(Inventory1,text='Inventory!')
tabcontrol1.pack(expand=1,fill="both")



#*********************************************************8



productId = ttk.Label(labelFrame,text="Product ID: ")
productId.config(font=("Courier",15))
productIdEntry = ttk.Entry(labelFrame)
productIdEntry.config(font=("Courier",20))
productIdEntry.grid(column=0,row=1,sticky='W')
productName = ttk.Label(labelFrame,text="Product Name : ")
productName.config(font=("Courier",15))
productNameEntry = ttk.Entry(labelFrame)
productNameEntry.config(font=("Courier",20))
productPrice = ttk.Label(labelFrame,text="Sell Price : ")
productPrice.config(font=("Courier",15))
productPriceEntry = ttk.Entry(labelFrame)
productPriceEntry.config(font=("Courier",20))
productPriceEntry.grid(column=0,row=5,sticky='W')
productQuantity = ttk.Label(labelFrame,text="Quantity : ")
productQuantity.config(font=("Courier",15))
productQuantityEntry = ttk.Entry(labelFrame)
productQuantityEntry.config(font=("Courier",20))
productQuantityEntry.grid(column=0,row=7,sticky="W")
InsertButton = ttk.Button(labelFrame,text='Insert',width=40)
ShowButton = ttk.Button(labelFrame,text='Show', width=40,command=Get_data)
UpdateButton = ttk.Button(labelFrame,text='Update',width=40)
DeleteButton = ttk.Button(labelFrame,text='Delete',width=40)
DeleteButton.grid(column=0,row=11,sticky='W',pady=7)
UpdateButton.grid(column=0,row=10,sticky='W',pady=7)
ShowButton.grid(column=0,row=9,sticky='W',pady=7)
InsertButton.grid(column=0,row=8,sticky='W', pady=7)
productQuantity.grid(column=0,row=6,sticky="W")
productPrice.grid(column=0,row=4,sticky='W')
productNameEntry.grid(column=0,row=3,sticky='W')
productName.grid(column=0,row=2,sticky='W')
productId.grid(column=0,row=0,sticky='W')
tabcontrol.add(Inventory,text='Inventory')
tabcontrol.pack(expand=1,fill="both")
#****************************************************************



root.mainloop()