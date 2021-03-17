from DBConnection import mysqlconnect
import tkinter.messagebox as tkMessageBox
from tkinter import *
import mysql.connector
from mysql.connector import Error
 
root = Tk()
root.title("Registration form")
width = 640
height = 640
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
 
 
#=======================================VARIABLES=====================================
CompanyName = StringVar()
CompanyAddress = StringVar()
CompanyPrice = StringVar()
ContactPhNo = StringVar()
PurchaseType = StringVar()
CompanyEmail = StringVar()
NoFeverID = StringVar()
#=======================================METHODS=======================================
 
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
 
 
def Register():
    
    # Connecting to the database
    conn = mysqlconnect()

    # Getting the cursor
    cursor = conn.cursor()

    if CompanyName.get == "" or CompanyAddress.get() == "" or Price.get() == "" or ContactPhNo.get == "" or PurchaseType.get == "" or Email.get == "" or NoFeverID.get == "":
        lbl_result.config(text="Please complete the required fields!", fg="orange")

    else:
        cursor.execute("INSERT INTO Adminstration (CompanyName, CompanyAddress, Price, ContactPhNo, PurchaseType, Email, NoFeverID) VALUES(%s, %s, %s, %s, %s, %s, %s)", (str(CompanyName.get()), str(CompanyAddress.get()), str(Price.get()), str(ContactPhNo.get()), str(PurchaseType.get()), str(Email.get()), str(NoFeverID.get())))
        conn.commit()
        CompanyName.set("")
        CompanyAddress.set("")
        CompanyPrice.set("")
        ContactPhNo.set("")
        PurchaseType.set("")
        CompanyEmail.set("")
        NoFeverID.set("")
        lbl_result.config(text="Successfully Created!", fg="green")
    cursor.close()
    conn.close()
 

 
#=====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)
 
 
#=====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="Input the information into the text fields below", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_CompanyName = Label(RegisterFrame, text="Company Name:", font=('arial', 18), bd=18)
lbl_CompanyName.grid(row=1)
lbl_CompanyAddress = Label(RegisterFrame, text="Company Address:", font=('arial', 18), bd=18)
lbl_CompanyAddress.grid(row=2)
lbl_Price = Label(RegisterFrame, text="Price:", font=('arial', 18), bd=18)
lbl_Price.grid(row=3)
lbl_CompanyPhone = Label(RegisterFrame, text="Company Phone:", font=('arial', 18), bd=18)
lbl_CompanyPhone.grid(row=4)
lbl_PurchaseType = Label(RegisterFrame, text="Purchase Type:", font=('arial', 18), bd=18)
lbl_PurchaseType.grid(row=5)
lbl_Email = Label(RegisterFrame, text="Company Email:", font=('arial', 18), bd=18)
lbl_Email.grid(row=6)
lbl_NoFeverID = Label(RegisterFrame, text="NoFeverID:", font=('arial', 18), bd=18)
lbl_NoFeverID.grid(row=7)

lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=8, columnspan=2)
 
 
#=======================================ENTRY WIDGETS===========================
CN = Entry(RegisterFrame, font=('arial', 20), textvariable=CompanyName, width=15)
CN.grid(row=1, column=1)
CA = Entry(RegisterFrame, font=('arial', 20), textvariable=CompanyAddress, width=15)
CA.grid(row=2, column=1)
Price = Entry(RegisterFrame, font=('arial', 20), textvariable=CompanyPrice, width=15)
Price.grid(row=3, column=1)
CPN = Entry(RegisterFrame, font=('arial', 20), textvariable=ContactPhNo, width=15)
CPN.grid(row=4, column=1)
PT = Entry(RegisterFrame, font=('arial', 20), textvariable=PurchaseType, width=15)
PT.grid(row=5, column=1)
Email = Entry(RegisterFrame, font=('arial', 20), textvariable=CompanyEmail, width=15)
Email.grid(row=6, column=1)
NFID = Entry(RegisterFrame, font=('arial', 20), textvariable=NoFeverID, width=15)
NFID.grid(row=7, column=1)
#========================================BUTTON WIDGETS=========================
btn_register=Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
btn_register.grid(row=9, columnspan=2)
#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
 
 
#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()