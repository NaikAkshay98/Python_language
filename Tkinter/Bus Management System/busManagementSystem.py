from tkinter import * #GUI package
from tkinter import ttk  
import sqlite3 as sq #For tables and database
import datetime

window = Tk()
window.title("B.E.S.T Management") 
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
#header = Label(window, text="Compound Tracker for Weightlifting", font=("arial",30,"bold"), fg="steelblue").pack()

con = sq.connect('busDB.db')
c = con.cursor() 

panedwindow = ttk.Panedwindow(window, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)
frame1 = ttk.Frame(panedwindow, height = 30)
panedwindow.add(frame1,weight = 4)

panedwindow_1 = ttk.Panedwindow(panedwindow, orient=VERTICAL)
panedwindow.add(panedwindow_1)
frame2 = ttk.Frame(panedwindow_1, width = 700, height = 380, relief = SUNKEN)
frame3 = ttk.Frame(panedwindow_1, width = 700, height = 60, relief = SUNKEN)

panedwindow_1.add(frame2, weight = 4)
panedwindow_1.add(frame3, weight = 4)

frame4 = ttk.Frame(panedwindow,height = 30)
panedwindow.add(frame4,weight = 4)
##############################################################################################################  switch
def bus():
    def busQuery():
        print("You have submitted a record")
        c.execute('CREATE TABLE IF NOT EXISTS bus (BusId INTEGER,BusNo INTEGER,BusDepot TEXT,BusCost INTEGER,BusManu TEXT,BusSerialNo INTEGER)') #SQL syntax
        c.execute('INSERT INTO bus (BusId,BusNo,BusDepot,BusCost,BusManu,BusSerialNo) VALUES (?,?,?,?,?,?)',(BusId.get(), BusNo.get(), BusDepot.get(),BusCost.get(),BusManu.get(),BusSerialNo.get())) #Insert record into database.
        con.commit()

        #Reset
        BusId.set('')
        BusNo.set('')
        BusDepot.set('')
        BusCost.set('')
        BusManu.set('')
        BusSerialNo.set('')
    #define
    BusId= StringVar(frame1)
    BusNo= StringVar(frame1)
    BusDepot= StringVar(frame1)
    BusCost= StringVar(frame1)
    BusManu= StringVar(frame1)
    BusSerialNo= StringVar(frame1)
    
    #labels
    L1 = Label(frame1, text = "BusId", font=("arial", 18)).place(x=10,y=100)
    L2 = Label(frame1, text = "BusNo ", font=("arial",18)).place(x=10,y=150)
    L3 = Label(frame1, text = "BusDepot ", font=("arial",18)).place(x=10,y=200)
    L4 = Label(frame1, text = "BusCost ", font=("arial",18)).place(x=10,y=250)
    L5 = Label(frame1, text = "BusManu ", font=("arial",18)).place(x=10,y=300)
    L6 = Label(frame1, text = "BusSerialNo", font=("arial",18)).place(x=10,y=350)

    #Entry for 'input' in GUI
    BusId_= Entry(frame1, textvariable=BusId)
    BusId_.place(x=220,y=155)

    BusNo_= Entry(frame1, textvariable=BusNo)
    BusNo_.place(x=220,y=205)

    BusDepot_= Entry(window, textvariable=BusDepot)
    BusDepot_.place(x=220,y=255)

    BusCost_= Entry(frame1, textvariable=BusCost)
    BusCost_.place(x=220,y=305)

    BusManu_= Entry(frame1, textvariable=BusManu)
    BusManu_.place(x=220,y=355)

    BusSerialNo_= Entry(frame1, textvariable=BusSerialNo)
    BusSerialNo_.place(x=220,y=405)

    button_1 = Button(frame1, text="Submit",command=busQuery)
    button_1.place(x=100,y=400)
def staff():
    def staffQuery():
        c.execute('CREATE TABLE IF NOT EXISTS staff (StaffId INTEGER,StaffName TEXT,StaffDesignation TEXT,BusId INTEGER)') #SQL syntax
        c.execute('INSERT INTO staff (StaffId,StaffName,StaffDesignation,BusId) VALUES (?,?,?,?)',(StaffId.get(), StaffName.get(), staffdb.get(),BusId.get())) #Insert record into database.

        if(staffdb.get()=="Driver"):
            c.execute('CREATE TABLE IF NOT EXISTS driver (DriverId INTEGER,DriverIdName TEXT,DriverSalary INTEGER)') #SQL syntax
            c.execute('INSERT INTO driver (DriverId,DriverIdName,DriverSalary) VALUES (?,?,?)',(StaffId.get(), StaffName.get(), Salary.get())) #Insert record into database.
        elif(staffdb.get()=="Conductor"):
            c.execute('CREATE TABLE IF NOT EXISTS conductor (ConductorId INTEGER,ConductorName TEXT,ConductorSalary INTEGER)') #SQL syntax
            c.execute('INSERT INTO conductor (ConductorId,ConductorName,ConductorSalary) VALUES (?,?,?)',(StaffId.get(), StaffName.get(), Salary.get())) #Insert record into database.
        elif(staffdb.get()=="TicketChecker"):
            c.execute('CREATE TABLE IF NOT EXISTS tc (TCId INTEGER,TCName TEXT,TCSalary INTEGER)') #SQL syntax
            c.execute('INSERT INTO tc (TCId,TCName,TCSalary) VALUES (?,?,?)',(StaffId.get(), StaffName.get(), Salary.get())) #Insert record into database.

        con.commit()

        StaffId.set('')
        StaffName.set('')
        BusId.set('')
        Salary.set('')
        staffdb.set('----')
        
                  
    StaffId= StringVar(frame1)
    StaffName= StringVar(frame1)
    #BusDepot= StringVar(frame1)
    Salary= StringVar(frame1)
    BusId= StringVar(frame1)

    L1 = Label(frame1, text = "StaffId", font=("arial", 18)).place(x=10,y=100)
    L2 = Label(frame1, text = "StaffName ", font=("arial",18)).place(x=10,y=150)
    L3 = Label(frame1, text = "StaffDesignation ", font=("arial",18)).place(x=10,y=200)
    L4 = Label(frame1, text = "Salary ", font=("arial",18)).place(x=10,y=300)
    L5 = Label(frame1, text = "BusId ", font=("arial",18)).place(x=10,y=350)

    StaffId_= Entry(frame1, textvariable=StaffId)
    StaffId_.place(x=220,y=155)

    StaffName_= Entry(frame1, textvariable=StaffName)
    StaffName_.place(x=220,y=205)

    #dropdown
    staffdb = StringVar(frame1)#2nd dropdown list
    staffdb.set('----')
    
    staff_comp = {'Driver', 'Conductor', 'TicketChecker'}
    staffdbase = OptionMenu(frame1, staffdb, *staff_comp)#For 2nd drop down list
    staffdbase.place(x=220,y=255)


    Salary_= Entry(window, textvariable=Salary)
    Salary_.place(x=220,y=355)

    BusId_= Entry(frame1, textvariable=BusId)
    BusId_.place(x=220,y=405)

    button_1 = Button(frame1, text="Submit",command=staffQuery)
    button_1.place(x=100,y=450)
def busno():
    def busnoQuery():
        print("You have submitted a record")
        c.execute('CREATE TABLE IF NOT EXISTS busno (BusNo INTEGER,BusStop INTEGER)') #SQL syntax
        c.execute('INSERT INTO busno (BusNo,BusStop) VALUES (?,?)',(BusNo.get(), BusStop.get())) #Insert record into database.
        con.commit()

        #Reset
        BusNo.set('')
        BusStop.set('')
        
    BusNo= StringVar(frame1)
    BusStop= StringVar(frame1)

    L1 = Label(frame1, text = "BusNo", font=("arial", 18)).place(x=10,y=100)
    L2 = Label(frame1, text = "BusStop", font=("arial",18)).place(x=10,y=150)

    BusNo_= Entry(frame1, textvariable=BusNo)
    BusNo_.place(x=220,y=155)

    BusStop_= Entry(frame1, textvariable=BusStop)
    BusStop_.place(x=220,y=205)

    button_1 = Button(frame1, text="Submit",command=busnoQuery)
    button_1.place(x=100,y=400)

def path():
    Busstopsh.set('')
    Lb1.delete(0,'end')
    ans2=('SELECT BusStop FROM busno WHERE BusNo=?')
    c.execute(ans2,[(BusNopath.get())])

    data = c.fetchall() 
    for row in data:
        Lb1.insert(1,row) 
    con.commit()

def bn():
    BusNopath.set('')
    Lb1.delete(0,'end')
    print(Busstopsh.get())
    ans1=('SELECT BusNo FROM busno WHERE BusStop=?')
    c.execute(ans1,[(Busstopsh.get())])
    
    data = c.fetchall() 
    for row in data:
        Lb1.insert(1,row) 
    con.commit()

BusNopath= StringVar(frame4)
BusNopath_= Entry(frame4, textvariable=BusNopath)
BusNopath_.place(x=100,y=20)

button_4 = Button(frame4, text="BUS NUMBER path",command=path)
button_4.place(x=100,y=40)

Busstopsh= StringVar(frame4)
Busstopsh_= Entry(frame4,textvariable=Busstopsh)
Busstopsh_.place(x=100,y=430)

button_4 = Button(frame4, text="BUS search",command=bn)
button_4.place(x=100,y=450)

pahframe= Frame(frame4)
pahframe.place(x=100, y = 60)
    
Lb1= Listbox(pahframe, height = 18, width = 8,font=("arial", 12)) 
Lb1.pack(side = LEFT, fill = Y)
    
scroll = Scrollbar(pahframe, orient = VERTICAL) 
scroll.config(command = Lb1.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb1.config(yscrollcommand = scroll.set) 

def tickprice():
    price=('SELECT tprice FROM ticket WHERE tsource=? AND tdest=?')
    c.execute(price,[(source.get()),(destn.get())])

    data = c.fetchall()
    L1 = Label(frame3, text =data, font=("arial", 18)).place(x=300,y=40)
    #for row in data:
     #   Lb1.insert(1,row) 
    con.commit()
L1 = Label(frame3, text = "SOURCE", font=("arial", 18)).place(x=10,y=40)
L2 = Label(frame3, text = "DESTINATION", font=("arial",18)).place(x=10,y=80)

source= StringVar(frame3)
source_= Entry(frame3, textvariable=source)
source_.place(x=200,y=40)

destn= StringVar(frame3)
destn_= Entry(frame3, textvariable=destn)
destn_.place(x=200,y=80)

tbutt= Button(frame3, text="Ticket Price",command=tickprice)
tbutt.place(x=10,y=120)
###############################################################################################################
#frame


def select(tablename):
    Lb.delete(0,'end')
    c.execute('SELECT * FROM '+tablename) 
    x=tablename
    if(x=="bus"):
        Lb.insert(0, 'BusId  BusNo  BusDepot  BusCost  BusManu  BusSerialNo ')
    elif(x=="staff"):
        Lb.insert(0, 'StaffId StaffName StaffDesignation BusId')
    elif(x=="driver"):
        Lb.insert(0, 'DriverId DriverIdName DriverSalary')
    elif(x=="conductor"):
        Lb.insert(0, 'ConductorId ConductorName ConductorSalary')
    elif(x=="tc"):
        Lb.insert(0, 'TCId TCName TCSalary')
    elif(x==""):
        Lb.insert(0, '')
    elif(x==""):
        Lb.insert(0, '')
    elif(x==""):
        Lb.insert(0, '')
    elif(x==""):
        Lb.insert(0, '')
    elif(x=="busno"):
        Lb.insert(0, 'BusNo  BusStop')
 
    data = c.fetchall()
    #code for spacing in table
    for i in range(len(data)):
        newlist=[]
        newlist=list(data[i])
        ans='           '.join(str(x) for x in newlist)
        
        Lb.insert(1,ans)
    con.commit()

frame = Frame(frame2)
frame.place(x=170, y =100)
    
Lb = Listbox(frame, height = 8, width = 50,font=("arial", 12)) 
Lb.pack(side = LEFT, fill = Y)
    
scroll = Scrollbar(frame, orient = VERTICAL) 
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb.config(yscrollcommand = scroll.set) 

compdb = StringVar(frame2)#2nd dropdown list
compdb.set('----')
    
compound = {'bus','staff','conductor','tc','driver','busno'}
compdbase = OptionMenu(frame2, compdb, *compound)#For 2nd drop down list
compdbase.place(x=500,y=500)

button_3 = Button(frame2,text="VIEW DB",command=lambda:select(compdb.get()))
button_3.place(x=400,y=500)

################################################################################################################


def delete(pkey):
    table=compdb.get()
    if(table=="bus"):
        c.execute('DELETE FROM bus WHERE BusId='+pkey)
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table=="OVH"):
        c.execute('DELETE FROM  WHERE =?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    elif(table==""):
        c.execute('DELETE FROM bus WHERE BusId=?',(pkey))
    pk.set('')
    con.commit()

pk= StringVar(frame2)
pk_= Entry(frame2, textvariable=pk)
pk_.place(x=360,y=405)
    
button_2 = Button(frame2,text="DELETE",command=lambda:delete(pk.get()))
button_2.place(x=300,y=500)

#####################################################################################################################
def update(table):
    tab=table
    win=Toplevel()
    win.title('Editing')
    win.geometry('300x300+10+10')
    def bussave():
        c.execute('UPDATE bus SET BusNo=?,BusDepot=?,BusCost=?,BusManu=?,BusSerialNo=? WHERE BusId=?',(NEWBusNo.get(),NEWBusDepot.get(),NEWBusCost.get(),NEWBusManu.get(),NEWBusSerialNo.get(),NEWBusId.get())) 
        con.commit()
        win.destroy()
    #BUS
    #BusId
    Label(win,text='BusId').place(x=0,y=0)
    NEWBusId=StringVar(win)
    Entry(win,textvariable=NEWBusId).place(x=110,y=0)
    #BusNo
    Label(win,text='NEW BusNo').place(x=0,y=40)
    NEWBusNo=StringVar(win)
    Entry(win,textvariable=NEWBusNo).place(x=110,y=40)
    #BusDepot
    Label(win,text='NEW BusDepot').place(x=0,y=80)
    NEWBusDepot=StringVar(win)
    Entry(win,textvariable=NEWBusDepot).place(x=110,y=80)
    #BusCost
    Label(win,text='NEW BusCost').place(x=0,y=120)
    NEWBusCost=StringVar(win)
    Entry(win,textvariable=NEWBusCost).place(x=110,y=120)
    #BusManu
    Label(win,text='NEW BusManu').place(x=0,y=160)
    NEWBusManu=StringVar(win)
    Entry(win,textvariable=NEWBusManu).place(x=110,y=160)
    #BusSerialNo
    Label(win,text='NEW BusSerialNo').place(x=0,y=200)
    NEWBusSerialNo=StringVar(win)
    Entry(win,textvariable=NEWBusSerialNo).place(x=110,y=200)

    button_4 = Button(win,text="SAVE",command=bussave)
    button_4.place(x=0,y=220)

    win.mainloop()
button_4= Button(frame2,text="EDIT",command=lambda:update(compdb.get()))
button_4.place(x=400,y=450)
######################################################################################################################


# buttons
button_1 = Button(window, text="BUS",command=bus,width=20)
button_1.place(x=0,y=0)
 
#button_1 = Button(window, text="BUS STOP",width=20)
#button_1.place(x=100,y=0)

button_1 = Button(window, text="STAFF",command=staff,width=20)
button_1.place(x=200,y=0)
'''
button_1 = Button(window, text="DRIVER",width=20)
button_1.place(x=300,y=0)

button_1 = Button(window, text="CONDUCTOR",width=20)
button_1.place(x=400,y=0)

button_1 = Button(window, text="TICKET CHECKER",width=20)
button_1.place(x=500,y=0)
'''
button_1 = Button(frame3, text="TICKETS",width=20)
button_1.place(x=150,y=0)

button_1 = Button(window, text="PASS DETAILS",width=20)
button_1.place(x=700,y=0)

button_1 = Button(window, text="ACCOUNT DETAILS",width=20)
button_1.place(x=800,y=0)

button_1 = Button(window, text="BUS MAINTAINACE",width=20)
button_1.place(x=900,y=0)

button_1 = Button(window, text="BUS NO",command=busno,width=20)
button_1.place(x=1000,y=0)

window.mainloop() 
