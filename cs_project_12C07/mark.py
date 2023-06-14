from functools import partial
from tkinter import *
from tkinter import messagebox
import login_page
import pymysql
from database_connection import host,password,database,user

#common variables:
color_1 = "#333333"
color_2 = "#FF3399"
color_3 = "#FFFFFF"
font="Arial"

#Button functions 
def AddStudent():
    global age_entrya
    global name_entrya
    global year_entrya
    global birth_entrya
    global course_entrya
    global email_entrya
    global subject_entrya
    global surname_entrya
    global gender_entrya
    global contact_entrya
    ClearScreen()

    name = Label(frame_1, text="First Name", font=(font,15,"bold"), bg=color_1,fg=color_3)
    name.place(x=40,y=30)
    name_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    name_entrya.place(x=40,y=60, width =200)

    surname = Label(frame_1,text="Last Name", font = (font,15,"bold"), bg=color_1,fg=color_3)
    surname.place(x=300,y=30)
    surname_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    surname_entrya.place(x=300,y=60,width=200)

    course = Label(frame_1, text="Course", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    course.place(x=40,y=100)
    course_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    course_entrya.place(x=40,y=130,width=200)

    subject = Label(frame_1, text="Subject", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    subject.place(x=300,y=100)
    subject_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    subject_entrya.place(x=300,y=130, width=200)

    year = Label(frame_1, text="Year", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    year.place(x=40,y=170)
    year_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    year_entrya.place(x=40,y=200, width=200)

    age = Label(frame_1, text="Age", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    age.place(x=300,y=170)
    age_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    age_entrya.place(x=300,y=200, width=200)

    gender = Label(frame_1, text="Gender", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    gender.place(x=40,y=240)
    gender_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    gender_entrya.place(x=40,y=270, width=200)

    birth = Label(frame_1, text="Birthday", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    birth.place(x=300,y=240)
    birth_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    birth_entrya.place(x=300,y=270, width=200)

    contact = Label(frame_1, text="Admission number", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    contact.place(x=40,y=310)
    contact_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    contact_entrya.place(x=40,y=340, width=200)

    email = Label(frame_1, text="Email", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    email.place(x=300,y=310)
    email_entrya = Entry(frame_1, bg=color_1, fg=color_3)
    email_entrya.place(x=300,y=340, width=200)

    submit_bt_1 = Button(frame_1, text='Submit', font=(font, 12), bd=2, command=Submit, cursor="hand2", bg=color_2,fg=color_3)
    submit_bt_1.place(x=200,y=389,width=100)
        

def GetContact_View():
    global getInfo_entry

    ClearScreen()
    getInfo = Label(frame_1, text="Enter Admission Number", font=(font, 18, "bold"), bg=color_1,fg=color_3)
    getInfo.place(x=140,y=70)
    getInfo_entry = Entry(frame_1, font=(font, 12), bg=color_1, fg=color_3,border=5)
    getInfo_entry.place(x=163, y=110, width=200, height=30)
    submit_bt_2 = Button(frame_1, text='Submit', font=(font, 10), bd=2, command=CheckContact_View, cursor="hand2", bg=color_2,fg=color_3)
    submit_bt_2.place(x=220,y=150,width=80)


def GetContact_Update():
    ClearScreen()
    global getInfo_entry

    getInfo = Label(frame_1, text="Enter Admission Number", font=(font, 18, "bold"), bg=color_1,fg=color_3)
    getInfo.place(x=140,y=70)
    getInfo_entry = Entry(frame_1, font=(font, 12), bg=color_1, fg=color_3,border=5)
    getInfo_entry.place(x=163, y=110, width=200, height=30)
    submit_bt_2 = Button(frame_1, text='Submit', font=(font, 10), bd=2, command=CheckContact_Update, cursor="hand2", bg=color_2,fg=color_3)
    submit_bt_2.place(x=220,y=150,width=80)


def GetContact_Delete():
    global getInfo_entry
    ClearScreen()

    getInfo = Label(frame_1, text="Enter Admission Number", font=(font, 18, "bold"), bg=color_1,fg=color_3)
    getInfo.place(x=140,y=70)
    getInfo_entry = Entry(frame_1, font=(font, 12), bg=color_1, fg=color_3,border=5)
    getInfo_entry.place(x=163, y=110, width=200, height=30)
    submit_bt_2 = Button(frame_1, text='Submit', font=(font, 10), bd=2, command=DeleteData, cursor="hand2", bg=color_2,fg=color_3)
    submit_bt_2.place(x=220,y=150,width=80)


def ClearScreen():
    for widget in frame_1.winfo_children():
            widget.destroy()


def Exit():
    window.destroy()


def Submit():
        if name_entrya.get() == "" or surname_entrya.get() == "" or course_entrya.get() == "" or subject_entrya.get() == "" or year_entrya.get() == "" or age_entrya.get() == "" or gender_entrya.get() == "" or birth_entrya.get() == "" or str(contact_entrya.get()) == "" or email_entrya.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=window)
        else:
            try:
                connection = pymysql.connect(host=host, user=user, password=password, database=database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", contact_entrya.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=window)
                else:
                    curs.execute("insert into student_register (f_name,l_name,course,subject,year,age,gender,birth,contact,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            name_entrya.get(),
                                            surname_entrya.get(),
                                            course_entrya.get(),
                                            subject_entrya.get(),
                                            year_entrya.get(),
                                            age_entrya.get(),
                                            gender_entrya.get(),
                                            birth_entrya.get(),
                                            contact_entrya.get(),
                                            email_entrya.get()  
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=window)


def CheckContact_View():
        if getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Admission number",parent=window)
        else:
            try:
                
                connection = pymysql.connect(host=host, user=user, password=password, database=database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Admission number doesn't exists",parent=window)
                else:
                    ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=window)


def CheckContact_Update():
    if getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Admission number",parent=window)
    else:
            try:
                
                connection = pymysql.connect(host=host, user=user, password=password, database=database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Admission number doesn't exists",parent=window)
                else:
                    GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=window)


def DeleteData():
    if getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Admission number",parent=window)
    else:
            try:
                
                connection = pymysql.connect(host=host, user=user, password=password, database=database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Admission number doesn't exists",parent=window)
                else:
                    curs.execute("delete from student_register where contact=%s", getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=window)


def ShowDetails(row):
        ClearScreen()
        name = Label(frame_1, text="First Name", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        name.place(x=40,y=30)
        name_data = Label(frame_1, text=row[0], font=(font, 10),bg=color_1,fg=color_3)
        name_data.place(x=40, y=60)

        surname = Label(frame_1, text="Last Name", font=(font, 15, "bold"),bg=color_1,fg=color_3)
        surname.place(x=300,y=30)
        surname_data = Label(frame_1, text=row[1], font=(font, 10),bg=color_1,fg=color_3)
        surname_data.place(x=300, y=60)

        course = Label(frame_1, text="Course", font=(font, 15, "bold"),bg=color_1,fg=color_3)
        course.place(x=40,y=100)
        course_data = Label(frame_1, text=row[2], font=(font, 10),bg=color_1,fg=color_3)
        course_data.place(x=40, y=130)

        subject = Label(frame_1, text="Subject", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        subject.place(x=300,y=100)
        subject_data = Label(frame_1, text=row[3], font=(font, 10),bg=color_1,fg=color_3)
        subject_data.place(x=300, y=130)

        year = Label(frame_1, text="Year", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        year.place(x=40,y=170)
        year_data = Label(frame_1, text=row[4], font=(font, 10),bg=color_1,fg=color_3)
        year_data.place(x=40, y=200)

        age = Label(frame_1, text="Age", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        age.place(x=300,y=170)
        age_data = Label(frame_1, text=row[5], font=(font, 10),bg=color_1,fg=color_3)
        age_data.place(x=300, y=200)

        gender = Label(frame_1, text="Gender", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        gender.place(x=40,y=240)
        gender_data = Label(frame_1, text=row[6], font=(font, 10),bg=color_1,fg=color_3)
        gender_data.place(x=40, y=270)

        birth = Label(frame_1, text="Birthday", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        birth.place(x=300,y=240)
        birth_data = Label(frame_1, text=row[7], font=(font, 10),bg=color_1,fg=color_3)
        birth_data.place(x=300, y=270)

        contact = Label(frame_1, text="Admission number", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        contact.place(x=40,y=310)
        contact_data = Label(frame_1, text=row[8], font=(font, 10),bg=color_1,fg=color_3)
        contact_data.place(x=40, y=340)

        email = Label(frame_1, text="Email", font=(font, 15, "bold"), bg=color_1,fg=color_3)
        email.place(x=300,y=310)
        email_data = Label(frame_1, text=row[9], font=(font, 10),bg=color_1,fg=color_3)
        email_data.place(x=300, y=340)


def GetUpdateDetails(row):
    global age_entry
    global name_entry
    global year_entry
    global birth_entry
    global course_entry
    global email_entry
    global subject_entry
    global surname_entry
    global gender_entry
    ClearScreen()

    name = Label(frame_1, text="First Name", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    name.place(x=40,y=30)
    name_entry = Entry(frame_1, bg=color_1, fg=color_3)
    name_entry.insert(0, row[0])
    name_entry.place(x=40,y=60, width=200)

    surname = Label(frame_1, text="Last Name", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    surname.place(x=300,y=30)
    surname_entry = Entry(frame_1, bg=color_1, fg=color_3)
    surname_entry.insert(0, row[1])
    surname_entry.place(x=300,y=60, width=200)

    course = Label(frame_1, text="Course", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    course.place(x=40,y=100)
    course_entry = Entry(frame_1, bg=color_1, fg=color_3)
    course_entry.insert(0, row[2])
    course_entry.place(x=40,y=130, width=200)

    subject = Label(frame_1, text="Subject", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    subject.place(x=300,y=100)
    subject_entry = Entry(frame_1, bg=color_1, fg=color_3)
    subject_entry.insert(0, row[3])
    subject_entry.place(x=300,y=130, width=200)

    year = Label(frame_1, text="Year", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    year.place(x=40,y=170)
    year_entry = Entry(frame_1, bg=color_1, fg=color_3)
    year_entry.insert(0, row[4])
    year_entry.place(x=40,y=200, width=200)

    age = Label(frame_1, text="Age", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    age.place(x=300,y=170)
    age_entry = Entry(frame_1, bg=color_1, fg=color_3)
    age_entry.insert(0, row[5])
    age_entry.place(x=300,y=200, width=200)

    gender = Label(frame_1, text="Gender", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    gender.place(x=40,y=240)
    gender_entry = Entry(frame_1, bg=color_1, fg=color_3)
    gender_entry.insert(0, row[6])
    gender_entry.place(x=40,y=270, width=200)

    birth = Label(frame_1, text="Birthday", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    birth.place(x=300,y=240)
    birth_entry = Entry(frame_1, bg=color_1, fg=color_3)
    birth_entry.insert(0, row[7])
    birth_entry.place(x=300,y=270, width=200)

    contact = Label(frame_1, text="Admission Number", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    contact.place(x=40,y=310)
    contact_data = Label(frame_1, text=row[8], font=(font, 10),bg=color_1,fg=color_3)
    contact_data.place(x=40, y=340)

    email = Label(frame_1, text="Email", font=(font, 15, "bold"), bg=color_1,fg=color_3)
    email.place(x=300,y=310)
    email_entry = Entry(frame_1, bg=color_1, fg=color_3)
    email_entry.insert(0, row[9])
    email_entry.place(x=300,y=340, width=200)

    submit_bt_1 = Button(frame_1, text='Submit', font=(font, 12), bd=2, command=partial(UpdateDetails, row), cursor="hand2", bg=color_2,fg=color_3)
    submit_bt_1.place(x=160,y=389,width=100)
    cancel_bt = Button(frame_1, text='Cancel', font=(font, 12), bd=2, command=ClearScreen, cursor="hand2", bg=color_2,fg=color_3)
    cancel_bt.place(x=280,y=389,width=100)

def UpdateDetails(row):
        if name_entry.get() == "" or surname_entry.get() == "" or course_entry.get() == "" or subject_entry.get() == "" or year_entry.get() == "" or age_entry.get() == "" or gender_entry.get() == "" or birth_entry.get() == "" or email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=window)
        else:
            try:
                connection = pymysql.connect(host=host, user=user, password=password, database=database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", row[8])
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The Admission number doesn't exists",parent=window)
                else:
                    curs.execute("update student_register set f_name=%s,l_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birth=%s, email=%s where contact=%s",
                                        (
                                            name_entry.get(),
                                            surname_entry.get(),
                                            course_entry.get(),
                                            subject_entry.get(),
                                            year_entry.get(),
                                            age_entry.get(),
                                            gender_entry.get(),
                                            birth_entry.get(),
                                            email_entry.get(),
                                            row[8]
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=window)

def reset_fields():
        name_entrya.delete(0, END)
        surname_entrya.delete(0, END)
        course_entrya.delete(0, END)
        subject_entrya.delete(0, END)
        year_entrya.delete(0, END)
        age_entrya.delete(0, END)
        gender_entrya.delete(0, END)
        birth_entrya.delete(0, END)
        contact_entrya.delete(0, END)
        email_entrya.delete(0, END)


#Change colour scheme
def main_pg():

    global window
    global frame_1
    global frame_2
    global add_bt
    global view_bt
    global update_bt
    global delete_bt
    global clear_bt
    global exit_bt
    
    window=Tk()
    window.title("Student Management System ")
    window.geometry("780x480")
    window.config(bg=color_1)
    #left frame
    frame_1=Frame(window,bg=color_1)
    frame_1.place(x=0,y=0,width =540,relheight=1)
    #right frame 
    frame_2=Frame(window,bg=color_1)
    frame_2.place(x=540,y=0,relwidth=1,relheight=1)

    #Buttons
    add_bt=Button(frame_2, text="Add New",font=(font,12),border=2,command=AddStudent,cursor="hand2",bg=color_2,fg=color_3)
    view_bt=Button(frame_2, text="View Details",font=(font,12),border=2,command=GetContact_View,cursor="hand2",bg=color_2,fg=color_3)
    update_bt = Button(frame_2, text="Update",font=(font,12),border=2,command=GetContact_Update,cursor="hand2",bg=color_2,fg=color_3)
    delete_bt = Button(frame_2, text="Delete",font=(font,12),border=2,command=GetContact_Delete,cursor="hand2",bg=color_2,fg=color_3)
    clear_bt = Button(frame_2, text="Clear",font=(font,12),border=2,command=ClearScreen,cursor="hand2",bg=color_2,fg=color_3)
    exit_bt = Button(frame_2, text="Exit",font=(font,12),border=2,command=Exit,cursor="hand2",bg=color_2,fg=color_3)
    #Place Buttons 
    add_bt.place(x=68,y=40,width=100)
    view_bt.place(x=68,y=100,width=100)
    update_bt.place(x=68,y=160,width=100)
    delete_bt.place(x=68,y=220,width=100)
    clear_bt.place(x=68,y=280,width=100)
    exit_bt.place(x=68,y=340,width=100)

    window.mainloop()