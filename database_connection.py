import pymysql

#Establishing connection to database
db_con=pymysql.connect(host='localhost',user='root',password="Joseph1234")
db_cur=db_con.cursor()
db_cur.execute("create database IF NOT EXISTS CS_project")
db_cur.execute("use Cs_project")
db_cur.execute("create table IF Not Exists auth (user_hash bigint primary key,user_Name varchar(30) unique,user_password varchar(16))")
db_cur.execute("create table IF NOt Exists student_register (f_name varchar(30),l_name varchar(30),course varchar(10),subject varchar(10),year int(4),age int(3),gender varchar(10),birth date ,contact int(10),email varchar(40))")
db_con.commit()
db_con.close()
host="localhost"
user ="root"
password="Joseph1234"
database="Cs_project"
#common variable to be used



