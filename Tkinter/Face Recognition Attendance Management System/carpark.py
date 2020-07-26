from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import sqlite3 as sq #For tables and database
global sub,dept,compdb
winhome = Tk()
winhome.title("Face_Recogniser")
#con = sq.connect('FaceBase.db')
con = sq.connect('FaceBase1.db')
c = con.cursor()
width=910
height=550
screen_width = winhome.winfo_screenwidth()
screen_height = winhome.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
winhome.geometry("%dx%d+%d+%d" % (width, height, x, y))
topFrame = Frame(winhome, width=910, height=40, bg="#ee5253")
bottomFrame = Frame(winhome, width=910, height=510, bg="#2d3436")
verticalFrame = Frame(winhome, width=5, height=900, bg="#ee5253")
topFrame.grid(row=0)
verticalFrame.place(x=450,y=0)
bottomFrame.grid(row=1)
winhome.overrideredirect(True)
winhome.resizable(0, 0)

class WindowDraggable():

    def __init__(self, Frame):
        self.topFrame = topFrame
        topFrame.bind('<ButtonPress-1>', self.StartMove)
        topFrame.bind('<ButtonRelease-1>', self.StopMove)
        topFrame.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None
        
    def OnMotion(self,event):
        x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
        y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
        winhome.geometry("+%s+%s" % (x, y))
WindowDraggable(topFrame)

#######################################################################################################################################################################################
#minimize button
def on_close(event=None):
    winhome.destroy()

def frame_mapped(event=None):
    winhome.update_idletasks()
    winhome.overrideredirect(True)
    winhome.state('normal')
topFrame.bind("<Map>",frame_mapped)

def on_minimize(event=None):
    winhome.update_idletasks()
    winhome.overrideredirect(False)
    winhome.state('iconic')

def on_entry_click_fname(event):
        """function that gets called whenever entry is clicked"""
        if username.get() == 'First Name':
           username.delete(0, "end") # delete all the text in the entry
           username.insert(0, '') #Insert blank for user input
def on_focus_out_fname(event):
        """function that gets called whenever entry is clicked"""
        if username.get() == '':
           username.insert(0, 'First Name') #Insert blank for user input
def on_entry_click_number(event):
        if number.get() == 'Roll no':
           number.delete(0, "end") # delete all the text in the entry
           number.insert(0, '') #Insert blank for user input
def on_focus_out_number(event):
        """function that gets called whenever entry is clicked"""
        if number.get() == '':
           number.insert(0, 'Roll no') #Insert blank for user input


#def previous():
  #  ms.showinfo(title="Scroll Down",message="enter your details!!!1")
   # return

def clear():
    username.delete(0, 'end')
    res = ""
    Notification.configure(text= res)
def clear1():
    number.delete(0, 'end')
    res = ""
    Notification.configure(text= res)
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
"""
winhome.bind_class("Entry","<FocusOut>",FocusOutHandler)
winhome.bind_class("Entry","<FocusIn>",FocusInHandler)
def FocusInHandler(event):
    text.insert("end","FocusIn %s\n" % event.widget)
    text.see("end")

def FocusOutHandler(event):
    text.insert("end","FocusOut %s\n" % event.widget)
    text.see("end")
"""
    
def TakeImages():        
    Id=(number.get())
    name=(username.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #method use to get values of rectangle
            faces = detector.detectMultiScale(gray, 1.3, 5)
            #print()
            font = cv2.FONT_HERSHEY_SIMPLEX 
            for (x,y,w,h) in faces:
                #method use to display phisical rectangle
                cv2.rectangle(img,(x,y),(x+w,y+h),(93,32,33),3)
                #print(sampleNum)
                #incrementing sample number 
                sampleNum=sampleNum+1
                #string to be displayed
                NumString=str(sampleNum)+"/61"
                cv2.putText(img,NumString,(x,y),font,1,(255,255,255),4)
                cv2.putText(img,"To quit press ENTER key",(100,y+h+70), font, 1,(0,0,0),3)
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('CAMERA',img)

            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('\r'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved \nID : " + Id +"\nName : "+ name
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        Note.configure(text= res)
    else:
        if(is_number(Id)==False):
            res ="Enter Appropriate Numeric Id"
            Note.configure(text= res)
        if(name.isalpha()==False):
            res ="Enter Appropriate Alphabetical Name"
            Note.configure(text= res)
        if(name.isalpha()==False & is_number(Id)==False):
            res ="Enter Appropriate Alphabetical Name and Numeric Id"
            Note.configure(text= res)

def TrainImages():
    recognizer=cv2.face_LBPHFaceRecognizer.create()

    #cv2.createLBPHFaceRecognizer()
    #cv2.face.createLBPHFaceRecognizer()
    #cv2.face.LBPHFaceRecognizer()
    #cv2.face.lbphfacerecognizercreate()
    #cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    #print(faces)
    #print(Id)
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    Note.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)
    print(df)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(93,32,33),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            #print(Id)
            #print(conf)
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                #print(df.loc[df['Id'] == Id]['Name'].values)
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='unknown'
                aa="['unknown']"
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h+20), font, 1,(255,255,255),2)
            cv2.putText(im,"To quit press ENTER key",(60,y+h+90), font, 1,(0,0,0),4)
            print(tt)
        attendance=attendance.drop_duplicates(subset=['Id'],keep='last')    
        cv2.imshow('Image tracking',im) 
        if (cv2.waitKey(1)==ord('\r')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    #Hour,Minute,Second=timeStamp.split(":")
    #fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    #attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    if(is_number(Id)==True):
        res=attendance
    else:
        res="Please try again"
    alldata.configure(text= res)

    #attendance table query
    #print(Id)
    #print(str(aa))
    #print(len(str(aa)))
    aa_str=str(aa)
    list1=[]
    #print(len(aa_str)-1)
    for i in range(len(aa_str)-1):
        list1.append(aa_str[i])
    #    print(list1)
    #print(list1)
    nau="".join(list1[2:len(aa_str)-2])
    #print(nau)

    print(sub.get())
    print(dept.get())
    print(compdb.get())
    if(Id!="unknown" and nau.islower()!="unknown"):
        c.execute('CREATE TABLE IF NOT EXISTS AllStudAtten (ID INTEGER,Name TEXT,Date TEXT,Time TEXT,Department TEXT,Semester TEXT,Subject TEXT)')
        #c.execute('CREATE TABLE IF NOT EXISTS AllStudAtten (ID INTEGER,Name TEXT,Date TEXT,Time TEXT)')
        c.execute('INSERT INTO AllStudAtten (ID,Name,Date,Time,Department,Semester,Subject) VALUES (?,?,?,?,?,?,?)',(Id,nau,date,timeStamp,dept.get(),compdb.get(),sub.get())) #Insert record into database.
        #c.execute('INSERT INTO AllStudAtten (ID,Name,Date,Time) VALUES (?,?,?,?)',(Id,nau,date,timeStamp)) #Insert record into database.
        con.commit()
       

#########################################################################################################################################################################
    #imageclose
image1 = Image.open("close.png")
image1 = image1.resize((25, 25), Image.ANTIALIAS) 
photo1 = ImageTk.PhotoImage(image1)
close = Button(winhome, image=photo1, borderwidth=0, bg="#ee5253", command=on_close) # button with image binded to the same function 
close.grid(row=0)
close.place( x=865, y=6)

#imagemin
image2 = Image.open("Mini.png")
image2 = image2.resize((25, 25), Image.ANTIALIAS) 
photo2 = ImageTk.PhotoImage(image2)
min1 = Button(winhome, image=photo2,  borderwidth=0, bg="#ee5253", command=on_minimize) # button with image binded to the same function 
min1.grid(row=0)
min1.place( x=840, y=6)

font1 = font.Font(family='Courier',weight="bold",size=17)

#Name
image3 = Image.open("user.png")
image3 = image3.resize((70, 70), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
previousbtn=Label(winhome, image=photo3,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70)
previousbtn.place(x=8,y=40)
#previouslbl=Label(winhome,text="BIKE_INFO",font=font1,bg="#2d3436",fg="#f64747")
#previouslbl.place(x=45,y=190)


label1=Label(topFrame,text="UserName")
entry1=Entry(topFrame)

helv36 = font.Font(family='Helvetica', size=13, weight='bold')
username = Entry(winhome, textvariable="username", font=helv36, bg="#2B2B37", fg="grey")
username.place( x=130, y=100, width=230, height=35)
username.bind('<FocusIn>', on_entry_click_fname)
username.bind('<FocusOut>', on_focus_out_fname)
username.insert(0,'First Name')

#Rollno
image4 = Image.open("Rollno.png")
image4 = image4.resize((70, 70), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)
Rollno=Label(winhome, image=photo4,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70)
Rollno.place(x=8,y=142)

helv36 = font.Font(family='Helvetica', size=13, weight='bold')
number= Entry(winhome, textvariable="Roll no", font=helv36,bg="#2B2B37", fg="grey")
number.place( x=130, y=190, width=230, height=35)
number.bind('<FocusIn>', on_entry_click_number)
number.bind('<FocusOut>', on_focus_out_number)
number.insert(0, 'Roll no')

#Notification
image5 = Image.open("iconfinder_JD.png")
image5 = image5.resize((70, 70), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)
Notification=Label(winhome, image=photo5,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70)
Notification.place(x=8,y=245)
#previouslbl=Label(winhome,text="Notification",font=font1,bg="#2d3436",fg="#f64747")
#previouslbl.place(x=45,y=190)


helv36 = font.Font(family='Helvetica', size=13, weight='bold')
Note=Label(winhome,borderwidth=0,bg="#2d3436",fg="white" ,width=140,height=140,padx=70,pady=70)
#Note = Entry(winhome, textvariable="Notification", font=helv36, bg="#2B2B37", fg="grey")
Note.place( x=130, y=290, width=230, height=45)

#Takephoto
image6 = Image.open("Camera.png")
image6 = image6.resize((70, 70), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)
Camera=Button(winhome, image=photo6,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70,command=TakeImages)
Camera.place(x=10,y=348)
Camera=Label(winhome,text="Capture",font=font1,bg="#2d3436",fg="#f64747")
Camera.place(x=25,y=460)


#Trainphoto
image7 = Image.open("training.png")
image7 = image7.resize((70, 70), Image.ANTIALIAS)
photo7 = ImageTk.PhotoImage(image7)
Train=Button(winhome, image=photo7,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70,command= TrainImages)
Train.place(x=200,y=350)
Train=Label(winhome,text="Train",font=font1,bg="#2d3436",fg="#f64747")
Train.place(x=240,y=460)


#Trackphoto
image8 = Image.open("iconfinder_image.png")
image8 = image8.resize((70, 70), Image.ANTIALIAS)
photo8 = ImageTk.PhotoImage(image8)
Track=Button(winhome, image=photo8,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70,command=TrackImages)
Track.place(x=600,y=350)
Track=Label(winhome,text="Trackpic",font=font1,bg="#2d3436",fg="#f64747")
Track.place(x=620,y=460)

#Attendace
image9 = Image.open("iconfinder_preferences-system-time.png")
image9 = image9.resize((70, 70), Image.ANTIALIAS)
photo9 = ImageTk.PhotoImage(image9)
Attend=Label(winhome, image=photo9,  borderwidth=0,bg="#2d3436" ,width=140,height=140,padx=70,pady=70)
Attend.place(x=468,y=40)
#previouslbl=Label(winhome,text="BIKE_INFO",font=font1,bg="#2d3436",fg="#f64747")
#previouslbl.place(x=45,y=190)


helv36 = font.Font(family='Helvetica', size=13, weight='bold')
alldata=Label(winhome,borderwidth=0,bg="#2d3436",fg="white" ,width=140,height=140,padx=70,pady=70)
#alldata= Entry(winhome, textvariable="Data", font=helv36, bg="#2B2B37", fg="grey")
alldata.place( x=580, y=75, width=260, height=70)
"""
#present and cancel button
cancel = Button(winhome, image=photo1, borderwidth=0, bg="#2d3436", command=on_close) # button with image binded to the same function
cancel.place( x=630, y=335)
present = Button(winhome, image=photo2, borderwidth=0, bg="#2d3436", command=on_close) # button with image binded to the same function
present.place( x=570, y=335)
"""
##########################################################DropDown
#2nd dropdown list
global dept
def deptVal(selection):
    if(selection in ["COMP","MECH","EXTC","IT","INSTRU"]) :
        print(dept.get())
        select()
    else:
        print("invalid")
        
dept=StringVar()
dept.set('DEPARTMENT')   
devalue =OptionMenu(winhome,dept, "COMP","MECH","EXTC","IT","INSTR",command=deptVal)#2ND drop down list
devalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
devalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
devalue.place(x=500,y=160,width=260,height=50)

#1ST dropdown list
global compdb
def varval(selection):
    print(selection)
    if(selection in ["SEM1","SEM2","SEM3","SEM4","SEM5","SEM6","SEM7","SEM8"]) :
        print(compdb.get())
        select()
    else:
        print("invalid")
    
compdb=StringVar()
compdb.set('SEMESTER')    
compdbase =OptionMenu(winhome,compdb, "SEM1","SEM2","SEM3","SEM4","SEM5","SEM6","SEM7","SEM8",command=varval)#1st drop down list
compdbase.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
compdbase['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
compdbase.place(x=500,y=220,width=130,height=50)

#3rd dropdown list
global sub

def select():
    print("reached")
    department=dept.get()
    semester=compdb.get()
    if((department in ["COMP","MECH","EXTC","IT","INSTRU"])and(semester=="SEM1")):
        sub.set('Subject')
        Svalue =OptionMenu(winhome,sub,"AM1","AP1","AC1","EM","BEE","EVS","BWP1",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department in ["COMP","MECH","EXTC","IT","INSTRU"])and(semester=="SEM2")):
        sub.set('Subject')
        Svalue =OptionMenu(winhome,sub,"AM2","AP2","AC2","ED","SPA","CS","BWP2",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM3")):
        Svalue =OptionMenu(winhome,sub,"AM3","DLDA","DM","ECCF","DS","OOPM",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM4")):
        Svalue =OptionMenu(winhome,sub,"AM4","AOA","COA","CG","OS","OST",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM5")):
        Svalue =OptionMenu(winhome,sub,"MP","DBMS","CN","TCS","AA","MM","AOS",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM6")):
        Svalue =OptionMenu(winhome,sub,"SE","SPCC","DWM","CSS","ML","ADBMS","ERP","ACN",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM7")):
        Svalue =OptionMenu(winhome,sub,"M7",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    elif((department=="COMP")and(semester=="SEM8")):
        Svalue =OptionMenu(winhome,sub,"M8",command=subVal)
        Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
        Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
        Svalue.place(x=500,y=280,width=260,height=50)
    
    else:
        print("invalid")
        

def subVal(selection):
    print(selection)
    if(selection in ["AM1","AP1","AC1","EM","BEE","EVS","BWP1","AM2","AP2","AC2","ED","SPA","CS","BWP2","AM3","DLDA","DM","ECCF","DS","OOPM","AM4","AOA","COA","CG","OS","OST","MP","DBMS","CN","TCS","AA","MM","AOS","SE","SPCC","DWM","CSS","ML","ADBMS","ERP","ACN","M7","M8"]) :
        print(sub.get())
    else:
        print("invalid")
sub=StringVar()
sub.set('Subject')
Svalue =OptionMenu(winhome,sub,"Enter \n Department and Semester")
Svalue.configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36,width=140,height=140,padx=70,pady=70)
Svalue['menu'].configure(borderwidth=0,bg="#2d3436",fg="white",font=helv36)
Svalue.place(x=500,y=280,width=260,height=50)
################################################################
clear
image10 = Image.open("close.png")
image10 = image10.resize((33,35), Image.ANTIALIAS) 
photo10 = ImageTk.PhotoImage(image10)
#clear button for name
clear= Button(winhome, image=photo10, borderwidth=0,bg="#2d3436", command=clear) # button with image binded to the same function 
clear.place( x=360, y=100)
#clear button for rollno
clear1= Button(winhome, image=photo10, borderwidth=0, bg="#2d3436", command=clear1) # button with image binded to the same function 
clear1.place( x=360, y=190)
