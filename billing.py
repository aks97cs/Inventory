global BILL_ID
global BILL_PRICE
global BILL_QT

BILL_ID = tk.StringVar()
BILL_PRICE = tk.StringVar()
BILL_QT = tk.StringVar()
global t

def Bill_add():
	db = sqlite3.connect('test.db')
	#db.execute('delete from temp')
	x = db.execute('select Quantity from stock where Product_Id = ?',[BILL_ID.get()])
	for y in x:
		t=y[0]
	t = int(t)
	y = int(BILL_QT.get())
	z= t-y
	db.execute('update stock set Quantity = ? where Product_Id = ?',[z,BILL_ID.get()])
	q = db.execute('select * from stock where Product_Id = ?',[BILL_ID.get()])
	for w in q:
		a = int(BILL_QT.get())
		a=int(a)
		b=w[2]
		b=int(b)
		db.execute('insert into temp values(?,?,?,?)',[w[0],w[1],w[2],a*b])
	db.commit()


def Bill_show():
	i=0
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from temp')
	tree1.delete(*tree1.get_children())
	for row in cursor:
		tree1.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3]))
		i=i+1


def Bill_total():
	db = sqlite3.connect("test.db")
	cursor = db.execute('select sum(Quantity) from temp')
	total = 0
	for row in cursor:
		total = row[0]
	print(total)
	tree1.insert('', 'end', text="---------", values=('----------','---------','Total = ',total))
	db.commit()

def Bill_print():
	db = sqlite3.connect('test.db')
	db.execute('delete from temp')
	db.commit()



