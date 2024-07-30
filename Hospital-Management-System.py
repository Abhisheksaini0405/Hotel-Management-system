from tkinter import *
import datetime
import time
from tkinter import messagebox
from tkinter import ttk
#from tkinter import _XYScrollCommand
import mysql.connector
#from tkinter.ttk import 
class Hospital:
    #==========fatch_data function for showing the data in bottom dataframe=======
    def fatch_data(self):
         conn = mysql.connector.connect(host = "localhost",username = "root",password = "root",database = "mydata")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from hospital")
         rows = my_cursor.fetchall()
         if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
            conn.commit()
         conn.close()
    #============ Making a function for exit =======================
    def iexit(self):
         iExit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
         if iExit > 0 :
              root.destroy()
              return 
    #============ Making a function for clear the data =============
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.injection.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.SideEfect.set("")
        self.FurtherInfomation.set("")
        self.Bloodpressure.set("")
        self.StorageDevice.set("")
        self.Medicine.set("")
        self.PatientId.set("")
        self.nhsnumber.set("")
        self.PatientName.set("")
        self.Nameiftablets.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        self.txt.delete("1.0",END)
    def iPrescriptionData(self):
            if self.Nameoftablets.get()=="" or self.ref.get() == "":
                messagebox.showerror("Error","All Fields are required")
            else:   
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "root",database = "mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                         self.ref.get(),
                                                                                                         self.Dose.get(),
                                                                                                         self.NumberofTablets.get(),
                                                                                                         self.Lot.get(),
                                                                                                         self.Issuedate.get(),
                                                                                                         self.Expdate.get(),
                                                                                                         self.DailyDose.get(),
                                                                                                         self.StorageDevice.get(),
                                                                                                         self.nhsnumber.get(),
                                                                                                         self.PatientName.get(),
                                                                                                         self.DateofBirth.get(),
                                                                                                         self.PatientAddress.get()
                                                                                                         ))
                messagebox.showinfo("Success","Record has been submitted")
                conn.commit()
                self.fatch_data()
                conn.close()
                #print("successfull")
    #========Make update function==============
    def update_data(self):
         conn = mysql.connector.connect(host = "localhost",username = "root",password = "root",database = "mydata")
         my_cursor = conn.cursor()
         my_cursor.execute("UPDATE hospital SET Nameoftablets = %s,dose=%s,Numberoftablets=%s,lot=%s,issueDate=%s,expDate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB =%s,patientaddress=%s WHERE Reference_No=%s",(     
                                                                                                self.Nameoftablets.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.Expdate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageDevice.get(),
                                                                                                self.nhsnumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateofBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                self.ref.get()
                                                                                            ))
         conn.commit()
         #print("Succes")
         #=========calling a function to show the updated data in dataframe============
         #self.iPrescriptionData()
         messagebox.showinfo("Success","Record has been updated")
         conn.close()  
         self.fatch_data()   
    #=========Making a presciption function for showing the data in presciption box.=============
    def presciptionbox(self):
         self.txt.insert(END,"Name of tablets:\t\t\t" + self.Nameoftablets.get()+"\n")
         self.txt.insert(END,"Reference No:\t\t\t" + self.ref.get()+"\n")
         self.txt.insert(END,"Dose:\t\t\t" + self.Dose.get()+"\n")
         self.txt.insert(END,"Number of tablets:\t\t\t" + self.NumberofTablets.get()+"\n")
         self.txt.insert(END,"Lot:\t\t\t" + self.Lot.get()+"\n")
         self.txt.insert(END,"Issue Date:\t\t\t" + self.Issuedate.get()+"\n")
         self.txt.insert(END,"Exp Date:\t\t\t" + self.Expdate.get()+"\n")
         self.txt.insert(END,"Side Effect:\t\t\t" + self.SideEfect.get()+"\n")
         self.txt.insert(END,"Further information:\t\t\t" + self.FurtherInfomation.get()+"\n")
         self.txt.insert(END,"Storage Adevice:\t\t\t" + self.StorageDevice.get()+"\n")
         self.txt.insert(END,"Patient ID:\t\t\t" + self.PatientId.get()+"\n")
         self.txt.insert(END,"NHS Number:\t\t\t" + self.nhsnumber.get()+"\n")
         self.txt.insert(END,"Patient Name:\t\t\t" + self.PatientName.get()+"\n")
         self.txt.insert(END,"Date of Birth:\t\t\t" + self.DateofBirth.get()+"\n")
         self.txt.insert(END,"Patient Address:\t\t\t" + self.PatientAddress.get()+"\n")
    #=============== Making a function for delete button ============
    def idelete(self):
         conn = mysql.connector.connect(host = "localhost",username = "root",password = "root",database = "mydata")
         my_cursor = conn.cursor()
         query = "delete from hospital where Reference_No = %s"
         value = (self.ref.get(),)
         my_cursor.execute(query,value)
         conn.commit()
         conn.close()
         messagebox.showinfo("Delete","Patient has been deleted successfully")  
         self.fatch_data()  
    #========== Making a function for moving back the data into fields when we focus on the bottom dataframe table ============
    def get_cursor(self,event=""):
         cursor_row = self.table.focus()
         content = self.table.item(cursor_row)
         row = content["values"]
         self.Nameoftablets.set(row[0])
         self.ref.set(row[1])
         self.Dose.set(row[2])
         self.NumberofTablets.set(row[3])
         self.Lot.set(row[4])
         self.Issuedate.set(row[5])
         self.Expdate.set(row[6])
         self.DailyDose.set(row[7])
         self.StorageDevice.set(row[8])
         self.nhsnumber.set(row[9])
         self.PatientName.set(row[10])
         self.DateofBirth.set(row[11])
         self.PatientAddress.set(row[12])
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.injection = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.SideEfect = StringVar()
        self.FurtherInfomation = StringVar()
        self.Bloodpressure = StringVar()
        self.StorageDevice= StringVar()
        self.Medicine = StringVar()
        self.PatientId = StringVar()
        self.nhsnumber = StringVar()
        self.PatientName = StringVar()
        self.Nameiftablets = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()
        l1=Label(self.root,bd=20,text="Hospital Manangement System",relief=RIDGE,fg="red",bg="black",font=("Times new roman",40))
        l1.pack(side=TOP,fill=X)    
        f1=Frame(self.root,bd=20,relief=RIDGE,padx=10)
        f1.place(x=0,y=100,height=400,width=1500)
        dataframe=LabelFrame(f1,text="Patience Information",padx=20,bd=10,relief=RIDGE,font=("Times new roman",10,"bold"))
        dataframe.place(x=0,y=5,height=350,width=980)
        dataframe1=LabelFrame(f1,padx = 20,text="Prescription",bd=10,relief=RIDGE,font=("Times new roman",10,"bold"))
        dataframe1.place(x=990,y=5,height=350,width=460)
        #----Make a Frame for buttons.------
        frmbtn=Frame(self.root,relief=RIDGE,bd=20)
        frmbtn.place(x=0,y=490,height=70,width=1500)
        #-----Details Frame--------
        frmdtb=Frame(self.root,relief=RIDGE,bd=20)
        frmdtb.place(x=0,y=560,height=200,width=1500)
        l1=Label(dataframe,text="Name of Tablets:",font=("arial",10),padx=2,pady=6)
        l1.grid(row=0,column=0,sticky="w")
        comnametablet=ttk.Combobox(dataframe,textvariable=self.Nameoftablets,state="readonly",font=("arial",11 ,"bold"),width=35)
        comnametablet['value']=("Amitriptyline","Corona Vacaine","Acetaminophen","Adderall","Ativan")
        comnametablet.current(0)
        comnametablet.grid(row=0,column=1)
        l2=Label(dataframe,text="Reference no:",font=("arial",10),padx=2,pady=6)
        l2.grid(row=1,column=0,sticky="w")
        e2=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        e2.grid(row=1,column=1)
        l3=Label(dataframe,text="Dose:",font=("arial",10),padx=2,pady=6)
        l3.grid(row=2,column=0,sticky="w")
        e3=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        e3.grid(row=2,column=1)
        l4=Label(dataframe,text="No of Tablets:",font=("arial",10),padx=2,pady=6)
        l4.grid(row=3,column=0,sticky="w")
        e4=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=35)
        e4.grid(row=3,column=1)
        l5=Label(dataframe,text="Lot:",font=("arial",10),padx=2,pady=6)
        l5.grid(row=4,column=0,sticky="w")
        e5=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        e5.grid(row=4,column=1)
        l6=Label(dataframe,text="Injection:",font=("arial",10),padx=2,pady=6)
        l6.grid(row=5,column=0,sticky="w")
        e6=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.injection,width=35)
        e6.grid(row=5,column=1)
        l7=Label(dataframe,text="Issue Date:",font=("arial",10),padx=2,pady=6)
        l7.grid(row=6,column=0,sticky="w")
        e7=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Issuedate,width=35)
        e7.grid(row=6,column=1)
        l8=Label(dataframe,text="Exp Date:",font=("arial",10),padx=2,pady=6)
        l8.grid(row=7,column=0,sticky="w")
        e8=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Expdate,width=35)
        e8.grid(row=7,column=1)
        l9=Label(dataframe,text="Daily Dose:",font=("arial",10),padx=2,pady=6)
        l9.grid(row=8,column=0,sticky="w")
        e9=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        e9.grid(row=8,column=1)
        l10=Label(dataframe,text="Side Effect:",font=("arial",10),padx=2,pady=6)
        l10.grid(row=9,column=0,sticky="w")
        e10=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.SideEfect,width=35)
        e10.grid(row=9,column=1)
        l11=Label(dataframe,text="Further Information:",font=("arial",10),padx=2,pady=6)
        l11.grid(row=0,column=2,sticky="w")
        e11=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.FurtherInfomation,width=25)
        e11.grid(row=0,column=3)
        l12=Label(dataframe,text="Blood Pressure:",font=("arial",10),padx=2,pady=6)
        l12.grid(row=1,column=2,sticky="w")
        e12=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Bloodpressure,width=25)
        e12.grid(row=1,column=3)
        l13=Label(dataframe,text="Storage Device:",font=("arial",10),padx=2,pady=6)
        l13.grid(row=2,column=2,sticky="w")
        e13=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.StorageDevice,width=25)
        e13.grid(row=2,column=3)
        l14=Label(dataframe,text="Medication:",font=("arial",10),padx=2,pady=6)
        l14.grid(row=3,column=2,sticky="w")
        e14=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.Medicine,width=25)
        e14.grid(row=3,column=3)
        l15=Label(dataframe,text="Patient ID:",font=("arial",10),padx=2,pady=6)
        l15.grid(row=4,column=2,sticky="w")
        e15=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.PatientId,width=25)
        e15.grid(row=4,column=3)
        l16=Label(dataframe,text="NHS Number:",font=("arial",10),padx=2,pady=6)
        l16.grid(row=5,column=2,sticky="w")
        e16=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.nhsnumber,width=25)
        e16.grid(row=5,column=3)
        l17=Label(dataframe,text="Patient Name:",font=("arial",10),padx=2,pady=6)
        l17.grid(row=6,column=2,sticky="w")
        e17=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.PatientName,width=25)
        e17.grid(row=6,column=3)
        l18=Label(dataframe,text="Date Of Birth:",font=("arial",10),padx=2,pady=6)
        l18.grid(row=7,column=2,sticky="w")
        e18=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.DateofBirth,width=25)
        e18.grid(row=7,column=3)
        l19=Label(dataframe,text="Patient Address:",font=("arial",10),padx=2,pady=6)
        l19.grid(row=8,column=2,sticky="w")
        e19=Entry(dataframe,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=25)
        e19.grid(row=8,column=3)
        #=============Make a presciption box ===================
        self.txt=Text(dataframe1,width = 65,height=20,bd=10,relief=RIDGE,font=("Times new roman",10))
        self.txt.grid(row = 0,column=0)
        #==========Make a Buttons ===========
        b1=Button(frmbtn,text="Presciption",command=self.presciptionbox,font=("Times",10,"bold"),width=33,bg = "lightblue",padx=2,pady=6)
        b1.grid(row=0,column=0)
        b2=Button(frmbtn,text="Presciption Data",font=("Times",10,"bold"),bg = "lightblue",width=33,padx=2,pady=6,command=self.iPrescriptionData)
        b2.grid(row=0,column=1)
        b3=Button(frmbtn,command=self.update_data,text="Update",font=("Times",10,"bold"),bg = "lightblue",width=32,padx=2,pady=6)
        b3.grid(row=0,column=2)
        b4=Button(frmbtn,text="Delete",command=self.idelete,font=("Times",10,"bold"),width=34,bg = "lightblue",padx=2,pady=6)
        b4.grid(row=0,column=3)
        b5=Button(frmbtn,text="Clear",command=self.clear,font=("Times",10,"bold"),width=33,bg = "lightblue",padx=2,pady=6)
        b5.grid(row=0,column=4)
        b6=Button(frmbtn,command=self.iexit,text="Exit",font=("Times",10,"bold"),width=34,bg = "lightblue",padx=2,pady=6)
        b6.grid(row=0,column=5)
        #=================Table============
        #==============Scrollbar======== 
        Yscroll=ttk.Scrollbar(frmdtb,orient=VERTICAL)
        Xscroll=ttk.Scrollbar(frmdtb,orient=HORIZONTAL)
        self.table=ttk.Treeview(frmdtb,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=Xscroll.set,yscrollcommand=Yscroll.set)
        Yscroll.pack(side=RIGHT,fill=Y)
        Xscroll.pack(side=BOTTOM,fill=X)
        Yscroll=ttk.Scrollbar(command=self.table.yview)
        Xscroll=ttk.Scrollbar(command=self.table.xview)
        self.table.heading("nameoftablets",text="Name of Tablets")
        self.table.heading("ref",text="Reference No.")
        self.table.heading("nooftablets",text="No. of Tablets")
        self.table.heading("lot",text="Lot")
        self.table.heading("issuedate",text="Issue Date")
        self.table.heading("dose",text="Dose")
        self.table.heading("expdate",text="Exp Date")
        self.table.heading("dailydose",text="Daily Dose")
        self.table.heading("storage",text="Storage")
        self.table.heading("nhsnumber",text="NHS Number")
        self.table.heading("pname",text="Patient Name")
        self.table.heading("dob",text="DOB")
        self.table.heading("address",text="Address")
        self.table.pack(expand=1,fill=BOTH)
        self.table["show"]="headings"
        self.table.column("nameoftablets",width=120)
        self.table.column("ref",width=100)
        self.table.column("dose",width=100)
        self.table.column("nooftablets",width=110)
        self.table.column("lot",width=100)
        self.table.column("issuedate",width=100)
        self.table.column("expdate",width=100)
        self.table.column("dailydose",width=100)
        self.table.column("storage",width=100)
        self.table.column("nhsnumber",width=100)
        self.table.column("pname",width=100)
        self.table.column("dob",width=100)
        self.table.column("address",width=100)
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        #==========Functionality Declaration===========
root = Tk()
ob = Hospital(root)
root.mainloop()