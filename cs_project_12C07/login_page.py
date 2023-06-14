import tkinter
from tkinter import messagebox
import log_in as log
import register_page
import mark

#result of login
login_OK=None

#function
def reg():
    window.withdraw()
    x=register_page.signup_win()
    
    
    

def logi():
    u=username_entry.get()
    p=password_entry.get()
    result=log.login(u,p)
    
    if result == 0:
        messagebox.showerror(title='login',message='User Name or Password is Empty')
    elif result == 1:
        messagebox.showerror(title="login",message="User does not EXIST")
    elif result == 2:
        messagebox.showinfo(title="login",message="successfully Loged IN")
        window.destroy()#this is used to minimise
        mark.main_pg()
        
    elif result == 3:
        messagebox.showerror(title="login",message="Password is incorrct")


def login_win():
    global window
    global password_entry
    global username_entry
    #Creation of window 
    window = tkinter.Tk()
    window.title("Login form")
    window.geometry('340x440')
    window.configure(bg='#333333')

    #creating a frame
    frame = tkinter.Frame(bg='#333333')

    #Creating widgets
    login_label = tkinter.Label(frame,text='Login',bg='#333333',fg="#FF3399",font=('Arial',30))
    username_label = tkinter.Label(frame, text='Username ',bg='#333333',fg="#FFFFFF",font=('Arial',16))
    username_entry = tkinter.Entry(frame,border=0,bg="#333333",fg="#FFFFFF",font=('Arial'))
    password_entry = tkinter.Entry(frame,show='*',border=0,bg="#333333",fg="#FFFFFF",font=('Arial'))
    password_label = tkinter.Label(frame,text='Password',bg='#333333',fg="#FFFFFF",font=('Arial',16))
    login_button = tkinter.Button(
        frame,text='Login',bg='#FF3399',fg='#FFFFFF',font=('arial',16),command=logi,cursor="hand2")
    signup_label = tkinter.Label(frame,text="Don't have a account ? ",border=0,bg="#333333",fg="#FFFFFF",font=("Arial",9))
    signup_button= tkinter.Button(
        frame,text="Sign up",bg="#333333",fg="#FF3399",cursor="hand2",font=("Arial",9),border=0,command=reg)
    tkinter.Frame(frame,height=1,width=135,bg="#FFFFFF").place(x=110,y=170)#line under the username
    tkinter.Frame(frame,height=1,width=135,bg="#FFFFFF").place(x=109,y=230)#line under the password
    tkinter.Label(frame,bg="#333333",width=0,height=1).grid(row=4,column=4)#place holder
    #widgit placement
    login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1,pady=20)
    password_label.grid(row =2, column=0)
    password_entry.grid(row=2, column=1,pady=20)
    login_button.grid(row=3, column=0, columnspan=2,pady=30)
    signup_label.place(x=47,y=348)
    signup_button.place(x=171,y=348)
    #340x440
    frame.pack()

    window.mainloop()

