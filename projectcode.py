#importing modules
import csv
import tkinter as tk
import mysql.connector
from tkinter import *

import mysql.connector as m



#Assigning Tkinted Object
root = Tk()

#Establishing MySQL- Python Connectivity
con=m.connect(host='127.0.0.1',user='root',password='amaatra',database='project')
cur=con.cursor()


#Fetching questions from MySQL
cur.execute("select * from personal_details")
data=list(cur.fetchall())
w=[]
hold=[]
for i in range (len(data)):
    w.append(data[i][1])
#print(w) -- test case

#Display screen dimentions 
root.geometry('1500x1500')
root.title("INFORMATION PORTAL")


#----------------------------------------------- FRONT END -----------------------------------------------------

#Header
l0 = Label(root, text="INFORMATION PORTAL",width=25, font=("Helvetica", 35))
l0.place(x=400,y=53)


#l1 and e1 -> Question 1 and Textbox
l1 = Label(root, text=w[0],width=20,font=("bold", 10))
l1.place(x=100,y=130)

e1 = Entry(root)
e1.place(x=700,y=130)

#e2 and l2 -> Question 2 and Text box
l2 = Label(root, text=w[1],width=20,font=("bold", 10))
l2.place(x=83,y=180)

e2 = Entry(root)
e2.place(x=700,y=180)

#l3 and radio -> Question 3 and Radio button
l3 = Label(root, text=w[2],width=20,font=("bold", 10))
l3.place(x=147,y=230)
var3 = IntVar()
Radiobutton(root, text="Uneducated",padx = 5, variable=var3, value=1).place(x=700,y=230)
Radiobutton(root, text="Matriculate",padx = 20, variable=var3, value=2).place(x=900,y=230)
Radiobutton(root, text="College Graduate",padx = 20, variable=var3, value=3).place(x=1100,y=230)

#l4 and e4 -> Question 4 and Text box
l4 = Label(root, text=w[3],width=25,font=("bold", 10))
l4.place(x=93,y=280)

e4 = Entry(root)
e4.place(x=700,y=280)

#l5 and radio -> Question 5 and Radio button
l5 = Label(root, text=w[4],width=20,font=("bold", 10))
l5.place(x=90,y=330)
var5 = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var5, value=1).place(x=700,y=330)
Radiobutton(root, text="Female",padx = 20, variable=var5, value=2).place(x=900,y=330)

#l6 and radio -> Question 6 and Radio button
l6 = Label(root, text=w[5],width=20,font=("bold", 10))
l6.place(x=115,y=380)
var6 = IntVar()
Radiobutton(root, text="N-E India",padx = 5, variable=var6, value=1).place(x=700,y=380)
Radiobutton(root, text="N India",padx = 20, variable=var6, value=2).place(x=900,y=380)
Radiobutton(root, text="S India",padx = 20, variable=var6, value=3).place(x=1100,y=380)

#l7 and e7 -> Question 7 and Text box
l7 = Label(root, text=w[6],width=50,font=("bold", 10))
l7.place(x=34,y=430)

e7 = Entry(root)
e7.place(x=700,y=430)

#l8 and radio -> Question 8 and Radio button
l8 = Label(root, text=w[7],width=40,font=("bold", 10))
l8.place(x=102,y=480)
var8 = IntVar()
Radiobutton(root, text="Speak",padx = 5, variable=var8, value=1).place(x=700,y=480)
Radiobutton(root, text="Read & Speak",padx = 20, variable=var8, value=2).place(x=900,y=480)
Radiobutton(root, text="Studied Language in School",padx = 20, variable=var8, value=3).place(x=1100,y=480)

#l9 and radio -> Question 9 and Radio button
l9 = Label(root, text=w[8],width=30,font=("bold", 10))
l9.place(x=73,y=530)
var9 = IntVar()
Radiobutton(root, text="Married",padx = 5, variable=var9, value=1).place(x=700,y=530)
Radiobutton(root, text="Unmarried",padx = 20, variable=var9, value=2).place(x=900,y=530)

#l10 and radio -> Question 10 and Radio button
l10 = Label(root, text=w[9],width=30,font=("bold", 10))
l10.place(x=75,y=580)
var10 = IntVar()
Radiobutton(root, text="Yes",padx = 5, variable=var10, value=1).place(x=700,y=580)
Radiobutton(root, text="No",padx = 20, variable=var10, value=2).place(x=900,y=580)

#-------------------------------------------------------------------------------------------------------------------




#--------------------------------------- BACK END / LOGIC ---------------------------------------------------

def recorddata():
    inform = Label(root, text = "Please look at IDLE output for job recommendations", width = 100, fg = "red", font = ("bold",10))
    inform.place(x=370,y=650)

#Storing user entered values entered into 'hold'
    hold.extend([e1.get(),e2.get(),var3.get(),e4.get(),var5.get(),var6.get(),e7.get(),var8.get(),var9.get(),var10.get()])

#Accepting only 10 digit values as phone numbers
    if (len(str(hold[3]))!=10):
        print("Enter a Valid Phone number of 10 digits")
        
    else:
        #print(hold) --test case

#Checking if phone number is present
        f=open("userInfo.csv")
        data=csv.reader(f)
        #print(data) --test case
        
        next(data)
        rows=[]
        for row in data:
            rows.append(row)
            
        #print(rows) --test case
        flag=0

        
#Using Phone Number as a unique identifier
        for i in range(len(rows)):
            if (rows[i]!=[]):
                if (rows[i][3]==hold[3]):
                    print("A form with this phone number already exists. Please give another phone number.")
                    flag=1
        f.close()
#Program ende      
        
        if (flag!=1):
            cs=ms=ss=0

# Checking Age
            if int(hold[1]) in range(18,30):
                ms=ms+1
            elif int(hold[1]) in range (30,50):
                ss=ss+1
            else:
                cs=cs+1

# Checking Education
            if hold[2] == 1:
                cs=cs+1
            elif hold[2] == 2:
                ss=ss+1
            else:
                ms=ms+1

# Checking Origin
            if hold[5] == 1:
                ms=ms+1
            elif hold[5] == 2:
                ss=ss+1
            else:
                cs=cs+1
# Checking Marital Status
            if hold[8]==1:
                cs=cs+1
                ss=ss+1
            else:
                ms=ms+1


# Checking Driver's License
            if hold[9]==1:
                ss+=1
            else:
                ms+=1
                cs+=1
            #print(cs,ms,ss) -- test case


#Incase the parameters become equal
            if ms == cs:
                if hold[2] == 1:
                    ms=ms+1
                else:
                    cs=cs+1
            elif ms == ss:
                if hold[2] == 3:
                    ss=ss+1
                else:
                    ms=ms+1


            elif cs == ss:
                if hold[2] == 3:
                    ss=ss+1
                else:
                    cs=cs+1

#Final result printing
            x = max(ms,cs,ss)
            jobRec=[]
            if x == ms:
                print("MANUFACTURING SECTOR")
                cur.execute("select * from manufacture")
                display = cur.fetchall()
                for i in range (len(display)):
                    jobRec.append(display[i][0])
            elif x == cs:
                print("CONSTRUCTION SECTOR")
                cur.execute("select * from construction")
                display = cur.fetchall()
                for i in range (len(display)):
                    jobRec.append(display[i][0])
            else:
                print("SERVICE SECTOR")
                cur.execute("select * from service")
                display = cur.fetchall()
                for i in range(len(display)):
                    jobRec.append(display[i][0])
            print("******** JOB RECOMMENDATIONS ********")
            for i in jobRec:
                print(i)
            print("*************************************")

            print("Thank you")


#Storing in CSV File
            f=open("userInfo.csv",'a')
            writerobj=csv.writer(f)
            #writerobj.writerow(['Name','Age','Level of Education','Phone number','Gender','Region','Number of Languages','Expertise inLanguage','Marital Status','Driving License']) ---test case
            writerobj.writerow(hold)
            f.close()
#------------------------------------------------------------------------------------------------------

#Submit button
btn=Button(root, text='Submit',width=20,bg='brown',fg='white', command=recorddata)
btn.place(x=700,y=620)

root.mainloop()

