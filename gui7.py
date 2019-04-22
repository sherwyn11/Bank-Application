from tkinter import *
import tkinter.messagebox
import sqlite3

conn=sqlite3.connect('Bank database1')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE BANK (ID INT PRIMARY KEY NOT NULL,ACCNO INT NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,CONTACT INT NOT NULL,ADDRESSPROOF TEXT NOT NULL,BALANCE INT NOT NULL,PASSWORD INT NOT NULL);''')

root=Tk()

class Bank:
    checkwork=0
    result=()
    checkpass=0
    update1=0
    reset=0
    depos=0
    res=[]
    n=[]
    flag=0
    check=0
    mainframe=Frame(root,height=200,width=250,pady=20,padx=20)
    newframe=Frame(root,height=200,width=250,pady=20,padx=20)
    defframe=Frame(root,height=200,width=250,pady=20,padx=20)
    wifframe=Frame(root,height=200,width=250,pady=20,padx=20)
    difframe=Frame(root,height=200,width=250,pady=20,padx=20)
    refframe=Frame(root,height=200,width=250,pady=20,padx=20)
    depframe=Frame(root,height=200,width=250,pady=20,padx=20)
    witframe=Frame(root,height=200,width=250,pady=20,padx=20)
    resframe=Frame(root,height=200,width=250,pady=20,padx=20)
    dispframe=Frame(root,height=200,width=250,pady=20,padx=20)

    flag1=0
    i=0
    acc=1000
    balance=500
    val=0
    def createAccount(self):
        Bank.mainframe.destroy()
        if(Bank.flag==2):
            print(Bank.flag)
            Bank.newframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.acc=Bank.acc+1
        Bank.flag=1
        a=Label(Bank.newframe,text="Account Creation Section: ")
        self.acc=Bank.acc
        self.balance=500
        self.name = StringVar()
        name1=Label(Bank.newframe,text="Enter Name: ")
        nin=Entry(Bank.newframe,textvariable=self.name)
        self.age = StringVar()
        age1=Label(Bank.newframe,text="Enter Age: ")
        ain=Entry(Bank.newframe,textvariable=self.age)
        self.contact = StringVar()
        contact1=Label(Bank.newframe,text="Enter Contact: ")
        cin=Entry(Bank.newframe,textvariable=self.contact)
        self.aproof = StringVar()
        #aproof1=Label(Bank.newframe,text="
        apin=Label(Bank.newframe,text="Enter Mode of Address Proof: ")
        variable=StringVar()
        variable.set("Choose")
        aproof1=OptionMenu(Bank.newframe,variable,"Aadhar Card","PAN Card","Other")
        self.pass1 = StringVar()
        p1=Label(Bank.newframe,text="Enter Password: ")
        p1in=Entry(Bank.newframe,show="*",width=10,textvariable=self.pass1)
        self.pass2 = StringVar()
        p2=Label(Bank.newframe,text="Confirm Password: ")
        p2in=Entry(Bank.newframe,show="*",width=10,textvariable=self.pass2)
        check=Checkbutton(Bank.newframe,text="I'm not a Robot",state='active')
        button =Button(Bank.newframe,text="Enter",pady=20,padx=20,command=self.empty)
        a.pack(fill="x")
        #acn.pack(fill="x")
        name1.pack(fill="x")
        nin.pack(fill="x")
        age1.pack(fill="x")
        ain.pack(fill="x")
        contact1.pack(fill="x")
        cin.pack(fill="x")
        apin.pack(fill="x")
        aproof1.pack(fill="x")
        p1.pack(fill="x")
        p1in.pack(fill="x")
        p2.pack(fill="x")
        p2in.pack(fill="x")
        check.pack(fill="x")
        button.pack(fill="x")
        Bank.newframe.pack(fill="x")

    def empty(self):
        Bank.flag1=0
        if not self.name.get():
            Bank.flag1=1
        elif not self.age.get():
            Bank.flag1=1
        elif not self.contact.get():
            Bank.flag1=1
        elif not self.pass1.get():
            Bank.flag1=1
        elif not (self.pass2.get()):
            Bank.flag1=1
        print(Bank.flag1)
        if(Bank.flag1==1):
            Bank.acc=Bank.acc-1
            tkinter.messagebox.showinfo('Error in details',"Please fill empty fields!")
        else:
            Bank.flag1=0
            self.message()



    def message(self):
        ans=tkinter.messagebox.askquestion('Confirm details',"Confirm details?")
        if(ans=='yes'):
            tkinter.messagebox.showinfo('New Account no.',"Congrats! Your account no. is: {}".format(Bank.acc))
            self.main()
        else:
            Bank.flag=2
            Bank.newframe.destroy()
            Bank.acc=Bank.acc-1
            self.createAccount()


    def dep(self,a):
        bal=0
        Bank.update1=1
        i=0
        Bank.defframe.destroy()
        Bank.check=1
        Bank.depframe=Frame(root,height=200,width=250,pady=20,padx=20)
        self.u=IntVar()
        acn=Label(Bank.depframe,text="Enter amount to be deposited:")
        ui=Entry(Bank.depframe,textvariable=self.u)
        print(Bank.result)
        x=int(self.u.get())
        print(type(x))
        print(x)
        print(self.u)
        self.acc=a
        Bank.n=[z[0] for z in Bank.res]
        print(bal)
        button =Button(Bank.depframe,text="Enter",pady=20,padx=20,command=self.main)
        acn.pack(fill="x")
        ui.pack(fill="x")
        button.pack(fill="x")
        Bank.depframe.pack(fill="x")

    def wh(self,a):
        Bank.check=1
        Bank.update1=2
        i=0
        Bank.wifframe.destroy()
        Bank.witframe=Frame(root,height=200,width=250,pady=20,padx=20)
        self.u=IntVar()
        acn=Label(Bank.witframe,text="Enter amount to be withdrawn:")
        ain=Entry(Bank.witframe,textvariable=self.u)
        print(Bank.result)
        x=int(self.u.get())
        print(type(x))
        print(x)
        print(self.u)
        print(self.balance)
        bal=x-self.balance
        self.acc=a
        Bank.n=[z[0] for z in Bank.res]
        print(bal)
        button =Button(Bank.witframe,text="Enter",pady=20,padx=20,command=self.main)
        acn.pack(fill="x")
        ain.pack(fill="x")
        button.pack(fill="x")
        Bank.witframe.pack(fill="x")

    def rs(self,a):
        Bank.refframe.destroy()
        Bank.resframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.check=1
        Bank.update1=3
        self.u=IntVar()
        acn1=Label(Bank.resframe,text="Enter new password:")
        ain1=Entry(Bank.resframe,show="*",width=10,textvariable=self.u)
        acn2=Label(Bank.resframe,text="Confirm new password:")
        ain2=Entry(Bank.resframe,show="*",width=10)
        Bank.n=[z[0] for z in Bank.res]
        self.acc=a
        button =Button(Bank.resframe,text="Enter",pady=20,padx=20,command=self.main)
        acn1.pack(fill="x")
        ain1.pack(fill="x")
        acn2.pack(fill="x")
        ain2.pack(fill="x")
        button.pack(fill="x")
        Bank.resframe.pack(fill="x")

    def checkAccount(self):
        i=0
        check=0
        Bank.checkpass=0
        Bank.res=[]
        Bank.result=()
        print(self.acc.get())
        print(self.pass1.get())
        a=int(self.acc.get())
        cursor.execute("SELECT ID,ACCNO,NAME,AGE,CONTACT,ADDRESSPROOF,BALANCE,PASSWORD FROM BANK WHERE ACCNO = (?)",(self.acc.get(),))
        Bank.result = cursor.fetchone()
        print(Bank.result)
        print("Check",Bank.checkpass)
        if(Bank.reset!=1):
            if(Bank.result!=None):
                if(int(Bank.result[7])!=int(self.pass1.get())):
                    print(int(Bank.result[7]))
                    print(type(Bank.result[7]))
                    print(type(self.pass1.get()))
                    Bank.checkpass=1
                else:
                    Bank.checkpass=0
            else:
                tkinter.messagebox.showinfo('Account error',"Account no. {} is not found (Incorrect Account no. or password)".format(self.acc.get()))
        else:
            if(Bank.result!=None):
                if(int(Bank.result[4])!=int(self.pass1.get())):
                    print(Bank.result[4])
                    print(type(Bank.result[4]))
                    print(type(self.pass1.get()))
                    Bank.checkpass=1
                else:
                    Bank.checkpass=0
            else:
                tkinter.messagebox.showinfo('Account error',"Account no. {} is not found (Incorrect Account no. or password)".format(self.acc.get()))

        print("Check",Bank.checkpass)
        if(Bank.result!=None and Bank.checkpass==0 and Bank.reset!=1):
            cursor.execute("SELECT BALANCE FROM BANK WHERE ACCNO = (?)",(self.acc.get(),))
            Bank.res.append(cursor.fetchone())
            print(Bank.res)
            if(Bank.chechwork==1):
                self.dep(a)
            elif(Bank.chechwork==2):
                self.wh(a)
            elif(Bank.chechwork==4):
                self.disp(a)
        elif(Bank.reset==1 and Bank.checkpass==0):
            if(Bank.chechwork==3):
                cursor.execute("SELECT PASSWORD FROM BANK WHERE ACCNO = (?)",(self.acc.get(),))
                Bank.res.append(cursor.fetchone())
                self.rs(a)
        else:
            tkinter.messagebox.showinfo('Account error',"Account no. {} is not found (Incorrect Account no. or password)".format(self.acc.get()))

    def deposit(self):
        Bank.mainframe.destroy()
        if(Bank.flag==2):
            print(Bank.flag)
            Bank.defframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.flag=1
        Bank.chechwork=1
        acn=Label(Bank.defframe,text="Enter Account no: ")
        ann=IntVar()
        ann=Entry(Bank.defframe)
        self.acc=ann
        pin=IntVar()
        p=Label(Bank.defframe,text="Enter Password:")
        pin=Entry(Bank.defframe,show="*",width=10)
        self.pass1=pin
        button =Button(Bank.defframe,text="Enter",pady=20,padx=20,command=self.checkAccount)
        acn.pack(fill="x")
        ann.pack(fill="x")
        p.pack(fill="x")
        pin.pack(fill="x")
        button.pack(fill="x")
        Bank.defframe.pack(fill="x")

    def withdraw(self):
        Bank.mainframe.destroy()
        if(Bank.flag==2):
            Bank.witframe.destroy()
            print(Bank.flag)
            Bank.wifframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.flag=1
        Bank.chechwork=2
        acn=Label(Bank.wifframe,text="Enter Account no")
        ain=IntVar()
        ain=Entry(Bank.wifframe)
        self.acc=ain
        pin=IntVar()
        p=Label(Bank.wifframe,text="Enter Password: ")
        pin=Entry(Bank.wifframe,show="*",width=10)
        self.pass1=pin
        button =Button(Bank.wifframe,text="Enter",pady=20,padx=20,command=self.checkAccount)
        acn.pack(fill="x")
        ain.pack(fill="x")
        p.pack(fill="x")
        pin.pack(fill="x")
        button.pack(fill="x")
        Bank.wifframe.pack(fill="x")

    def disp(self,b):
        Bank.difframe.destroy()
        Bank.dispframe=Frame(root,height=200,width=250,pady=20,padx=20)
        print(Bank.result)
        Bank.check=1
        a=Bank.result[1]
        acn1=Label(Bank.dispframe,text="Account No. :")
        acn2=Label(Bank.dispframe,text=a)
        a=Bank.result[2]
        acn3=Label(Bank.dispframe,text="Name : ")
        acn4=Label(Bank.dispframe,text=a)
        a=Bank.result[3]
        acn5=Label(Bank.dispframe,text="Age : ")
        acn6=Label(Bank.dispframe,text=a)
        a=Bank.result[4]
        acn7=Label(Bank.dispframe,text="Contact No. :")
        acn8=Label(Bank.dispframe,text=a)
        a=Bank.result[6]
        acn9=Label(Bank.dispframe,text="Current Balance :")
        acn10=Label(Bank.dispframe,text=a)
        button =Button(Bank.dispframe,text="OK",pady=20,padx=20,command=self.main)
        acn1.pack(fill="x")
        acn2.pack(fill="x")
        acn3.pack(fill="x")
        acn4.pack(fill="x")
        acn5.pack(fill="x")
        acn6.pack(fill="x")
        acn7.pack(fill="x")
        acn8.pack(fill="x")
        acn9.pack(fill="x")
        acn10.pack(fill="x")
        button.pack(fill="x")
        Bank.dispframe.pack(fill="x")



    def display(self):
        Bank.mainframe.destroy()
        if(Bank.flag==2):
            print(Bank.flag)
            Bank.difframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.flag=1
        Bank.chechwork=4
        acn=Label(Bank.difframe,text="Enter Account no: ")
        ain=IntVar()
        ain=Entry(Bank.difframe)
        self.acc=ain
        p=Label(Bank.difframe,text="Enter Password: ")
        pin=IntVar()
        pin=Entry(Bank.difframe,show="*",width=10)
        self.pass1=pin
        button =Button(Bank.difframe,text="Enter",pady=20,padx=20,command=self.checkAccount)
        acn.pack(fill="x")
        ain.pack(fill="x")
        p.pack(fill="x")
        pin.pack(fill="x")
        button.pack(fill="x")
        Bank.difframe.pack(fill="x")



    def reset(self):
        Bank.mainframe.destroy()
        if(Bank.flag==2):
            print(Bank.flag)
            Bank.refframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.flag=1
        Bank.reset=1
        Bank.chechwork=3
        acn=Label(Bank.refframe,text="Enter Account no: ")
        ain=IntVar()
        ain=Entry(Bank.refframe)
        self.acc=ain
        pin=IntVar()
        p=Label(Bank.refframe,text="Enter Contact no: ")
        pin=Entry(Bank.refframe)
        self.pass1=pin
        button =Button(Bank.refframe,text="Enter",pady=20,padx=20,command=self.checkAccount)
        acn.pack(fill="x")
        ain.pack(fill="x")
        p.pack(fill="x")
        pin.pack(fill="x")
        button.pack(fill="x")
        Bank.refframe.pack(fill="x")

    def main(self):
        if(Bank.flag==1):
            Bank.val=0
            Bank.i=Bank.i+1
            print(self.name.get())
            print(self.age.get())
            print(self.contact.get())
            print(self.aproof.get())
            if(Bank.check==0):
                cursor.execute("INSERT INTO BANK (ID,ACCNO,NAME,AGE,CONTACT,ADDRESSPROOF,BALANCE,PASSWORD)VALUES(?,?,?,?,?,?,?,?)",(Bank.i,self.acc,self.name.get(),self.age.get(),self.contact.get(),self.aproof.get(),self.balance,self.pass1.get()));
                conn.commit()
            Bank.flag=Bank.flag+1
            print(Bank.flag)
            Bank.newframe.destroy()
            Bank.defframe.destroy()
            Bank.depframe.destroy()
            Bank.wifframe.destroy()
            Bank.difframe.destroy()
            Bank.refframe.destroy()
            Bank.witframe.destroy()
            Bank.resframe.destroy()
            Bank.dispframe.destroy()
            Bank.mainframe=Frame(root,height=200,width=250,pady=20,padx=20)
        Bank.check=0

        if(Bank.update1==1):
            p=Bank.n[0]
            Bank.update1=0
            p=p+int(self.u.get())
            Bank.n.append(p)
            print(Bank.n)
            print(type(Bank.n[0]))
            cursor.execute("UPDATE BANK SET BALANCE = (?) WHERE BALANCE=(?) AND ACCNO =(?)" ,(Bank.n[1],Bank.n[0],self.acc))
            conn.commit()
            Bank.n=[]

        elif(Bank.update1==2):
            q=Bank.n[0]
            Bank.update1=0
            if(int(self.u.get())>q):
                tkinter.messagebox.showinfo('Insufficient funds',"You have insufficent balance to withdraw from")
            else:
                q=q-int(self.u.get())
                Bank.n.append(q)
                print(type(Bank.n[0]))
                print(Bank.n)
                cursor.execute("UPDATE BANK SET BALANCE = (?) WHERE BALANCE=(?) AND ACCNO =(?)" ,(Bank.n[1],Bank.n[0],self.acc))
                conn.commit()
                Bank.n=[]

        elif(Bank.update1==3):
            print(Bank.n)
            Bank.update1=0
            Bank.reset=0
            a=self.u.get()
            Bank.n.append(a)
            print(Bank.n)
            cursor.execute("UPDATE BANK SET PASSWORD = (?) WHERE PASSWORD=(?) AND ACCNO =(?)" ,(Bank.n[1],Bank.n[0],self.acc))
            conn.commit()
            Bank.n=[]


        label=Label(Bank.mainframe,text="WELCOME TO SOME BANK",pady=20,padx=20)
        button1 =Button(Bank.mainframe,text="Create a new Account",pady=20,command=self.createAccount)
        button2 =Button(Bank.mainframe,text="Deposit",pady=20,padx=20,command=self.deposit)
        button3 =Button(Bank.mainframe,text="Withdraw",pady=20,padx=20,command=self.withdraw)
        button4 =Button(Bank.mainframe,text="Display details",pady=20,padx=20,command=self.display)
        button5 =Button(Bank.mainframe,text="Reset Password",pady=20,padx=20,command=self.reset)
        button6 =Button(Bank.mainframe,text="Quit",pady=20,padx=20,command=self.Quit)
        label.pack(fill="x")
        button1.pack(fill="x")
        button2.pack(fill="x")
        button3.pack(fill="x")
        button4.pack(fill="x")
        button5.pack(fill="x")
        button6.pack(fill="x")
        Bank.mainframe.pack(fill="x")


    def Quit(self):
        conn.close()
        exit(0)
        mainframe.destroy()
        root.mainloop()





b=Bank()
b.main()
root.mainloop()
