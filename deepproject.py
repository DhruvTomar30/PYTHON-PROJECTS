import mysql.connector
from tabulate import tabulate

root = mysql.connector.connect(host = "localhost" , user = "root" , password = "tomar@12345*", port=3307)
root_ = root.cursor()

sql = "CREATE DATABASE IF NOT EXISTS COLLEGE_MANAGEMENT_SYSTEM;"
root_.execute(sql)

sql = "USE COLLEGE_MANAGEMENT_SYSTEM;"
root_.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS STUDENT(R_NO INT(5) PRIMARY KEY , NAME VARCHAR(200) , AGE INT(3) , COURSE VARCHAR(10));"
root_.execute(sql)

def data_insert():
    name = input("ENTER THE STUDENT NAME:-")
    age = int(input("ENTER THE STUDENT AGE:-"))
    course = str(input("ENTER THE STUDENT'S COURSE:-"))
    sql = "SELECT * FROM STUDENT;"
    root_.execute(sql)
    records =root_.fetchall()
    start = len(records)+1
    sql = "INSERT INTO STUDENT VALUES(%s,%s,%s,%s);"
    val = (start,name,age,course)
    root_.execute(sql,val)
    root.commit()
    print(".....DATA ADDED SUCCESSFULLY.....")

def data_update():
    updation = input("Field you want to update(COURSE/AGE/NAME):-")
    R_NO = int(input("STUDENT'S ROLL NUMBER:- "))
    new_val = input("NEW VALUE:-")
    sql = f"UPDATE STUDENT SET {updation} = '{new_val}' WHERE R_NO = {R_NO};"
    root_.execute(sql)
    root.commit()
    print(".....RECORD UPDATED.....")

def data_delete():
    R_NO = int(input("Student's Roll number:-"))
    sql = f"DELETE FROM STUDENT WHERE R_NO = {R_NO};"
    root_.execute(sql)
    root.commit()
    print(".....RECORD DELETED.....")

def data_search():
    print("1.SEARCH BY STUDENT ROLL NUMBER ID\n2.SEARCH BY NAME\n3.SEARCH BY COURSE")
    choicee = int(input("ENTER THE CHOICE(1-3):-"))
    if choicee == 1:
        R_NO = input("ENTER STUDENT ROLL NUMBER:-")
        sql = f"SELECT * FROM STUDENT WHERE R_NO = {R_NO};"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["ROLL NUMBER","NAME","AGE","COURSE"]))
    elif choicee == 2:
        name = input("ENTER THE STUDENT NAME:-")
        sql = f"SELECT * FROM STUDENT WHERE NAME = {name};"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["ROLL NUMBER","NAME","AGE","COURSE"]))
    elif choicee == 3:
        course = input("ENTER THE STUDENT COURSE:-")
        sql = f"SELECT * FROM STUDENT WHERE COURSE = {course}"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["ROLL NUMBER","NAME","AGE","COURSE"]))
    else:
        return

def data_display():
    sql = "SELECT * FROM STUDENT;"
    root_.execute(sql)
    records = root_.fetchall()
    print(tabulate(records,headers = ["ROLL NUMBER", "NAME","AGE","COURSE"]))

def menu():
    while True:
        print("\t\t\tMENU\t\t\t")
        print("TASK:-\n1.DATA INSERTION\n2.DATA UPDATION\n3.DATA DELETION\n4.DATA DISPLAY\n5.DATA SEARCH\n6.EXIT")
        choice = int(input("ENTER THE CHOICE(1-6):-"))
        if choice == 1:
            data_insert()
        elif choice == 2:
            data_update()
        elif choice == 3:
            data_delete()
        elif choice == 4:
            data_display()
        elif choice == 5:
            data_search()
        else:
            break
        print("\n\n\n")

menu()
root.close()

