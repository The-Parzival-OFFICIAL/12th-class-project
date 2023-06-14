from tkinter import *
import log_in
import login_page
from tkinter import messagebox
import pymysql as sql
def sign():
    user = user_entry.get()
    pasw= password_entry.get()
    re_pasw = re_password_entry.get()
    if user =='' or pasw == '':
        messagebox.showerror(title='ERROR',message="User Name or Password is Empty")
    
    elif user !="" and pasw!="" and re_pasw=="":
        messagebox.showerror(title="ERROR",message="Confirm your password")

    elif user !="" and re_pasw!=pasw:
        messagebox.showerror(title='ERROR',message='Password does not match!!')
  
    elif user!="" and pasw == re_pasw :
        x=log_in.signup(user,pasw)
        if x == 1:
            messagebox.showerror("ERORR",message="User Name already exists")
        else:
            messagebox.showinfo(title="Sign up",message="Successfuly registered")
            login_page.window.deiconify()
            root.destroy()
            
            

def signup_win():
    global root
    global user_entry 
    global password_entry
    global re_password_entry
    

    #Creation of window 
    root=Tk()
    root.title('Register',)
    root.geometry('340x440')
    root.config(bg='#333333')
    root.resizable(False,False)
    #creation of window 
    frame=Frame(root,bg="#333333")

    #widgit 
    lable=Label(frame,text="Sign up",bg="#333333",fg="#FF3399",font=('Arial',30))
    user_lable=Label(frame,text="Username",bg="#333333",fg="#FFFFFF",font=('Arial',16))
    user_entry=Entry(frame,bg="#333333",fg="#FFFFFF",font=("Arial"),border=0,width=16)
    password_lable=Label(frame,text="Password",bg="#333333",fg="#FFFFFF",font=("Arial",16))
    password_entry=Entry(frame,bg="#333333",fg="#FFFFFF",font=("Arial"),border=0,width=16,show="*")
    re_password_lable=Label(frame,text="Confirm Password",bg="#333333",fg="#FFFFFF",font=("Arial",14))
    re_password_entry=Entry(frame,bg="#333333",fg="#FFFFFF",font=("Arial"),border=0,width=16,show="*")
    signup_button=Button(frame,text="Sign up",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command=sign,cursor="hand2")
    Frame(frame,height=1,width=147,bg="#FFFFFF").place(x=171,y=170)#line under the username
    Frame(frame,height=1,width=147,bg="#FFFFFF").place(x=171,y=232)#line under the password
    Frame(frame,height=1,width=147,bg="#FFFFFF").place(x=171,y=294)#line under the confirm password
    Label(frame,bg="#333333",width=0,height=1).grid(row=5,column=4)#place holder
    #wigit position
    lable.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
    user_lable.grid(row=1,column=0)
    user_entry.grid(row=1,column=1,padx=8,pady=20)
    password_lable.grid(row=2,column=0)
    password_entry.grid(row=2,column=1,pady=20)
    re_password_lable.grid(row=3,column=0)
    re_password_entry.grid(row=3,column=1,pady=20)
    signup_button.grid(row=4,column=0,columnspan=2,pady=30)

    frame.pack()


    root.mainloop()


