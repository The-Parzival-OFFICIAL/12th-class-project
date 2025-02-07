from pymysql import *
from random import randint

#login authinticator
def login(u,input_pw):
    
    if u=="" or input_pw=="":
        return 0 # user or pwd empty
    is_user_available=False
    con=connect(host="localhost",user='root',password="root",database="Cs_project")
    cur=con.cursor()
    cur.execute("select * from auth")
    al=cur.fetchall()
    for i in al:
        if u == i[1]:
            is_user_available=True
            break
        else:
            is_user_available=False
    if is_user_available ==False:
        con.close()
        return 1 # user is not registred 
    else:
        query="select user_password from auth where user_Name='{}'"
        cur.execute(query.format(u))
        DB_pw =cur.fetchone()[0]
        
        if input_pw==DB_pw:
            con.close()
            return 2 # user successfully logged in
        else:
            con.close()
            return 3 #user and password wrong
    

def signup(user,pasw):
    con=connect(host="localhost",user='root',password="root",database="Cs_project")
    cur=con.cursor()
    cur.execute("select * from auth")
    al=cur.fetchall()
    is_user_availabl=False
    for i in al:
        if user== i[1]:
            is_user_availabl=True
            
            break
        else:
           
            is_user_availabl=False
    if is_user_availabl==True:
        con.close()
        return 1 # user already exists 
    
    elif is_user_availabl ==False: # user is not registred
        x=randint(0,999999999)
        query="insert into auth values ({},'{}','{}')"
        cur.execute(query.format(x,user,pasw))
        con.commit()
        con.close()
        

    
