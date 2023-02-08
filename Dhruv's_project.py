import mysql.connector
from tabulate import tabulate

root = mysql.connector.connect(host = "localhost" , user = "root" , password = "tomar@12345*", port=3307)
root_ = root.cursor()

root_.execute("CREATE DATABASE IF NOT EXISTS EMPLOYEE_MANAGEMENT_SYSTEM;")


sql = "USE EMPLOYEE_MANAGEMENT_SYSTEM;"
root_.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS EMPLOYEE(E_ID INT(5) PRIMARY KEY , NAME VARCHAR(200) , AGE INT(3) , SALARY FLOAT(10) , DESIGNATION VARCHAR(200));"
root_.execute(sql)

def data_insert():
    name = input("ENTER THE EMPLOYEE NAME:-")
    age = int(input("ENTER THE EMPLOYEE AGE:-"))
    salary = float(input("ENTER THE EMPLOYEE SALARY:-"))
    desig = input("ENTER THE EMPLOYEE DESIGNATION:-")
    sql = "SELECT * FROM EMPLOYEE;"
    root_.execute(sql)
    records =root_.fetchall()
    start = len(records)+1
    sql = "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s);"
    val = (start,name,age,salary,desig)
    root_.execute(sql,val)
    root.commit()
    print(".....DATA ADDED SUCCESSFULLY.....")

def data_update():
    updation = input("Field you want to update(SALARY/DESIGNATION/AGE/NAME):-")
    E_ID = int(input("EMPLOYEE ID:-"))
    new_val = input("NEW VALUE:-")
    sql = f"UPDATE EMPLOYEE SET {updation} = '{new_val}' WHERE E_ID = {E_ID};"
    root_.execute(sql)
    root.commit()
    print(".....RECORD UPDATED.....")

def data_delete():
    E_ID = int(input("EMPLOYEE ID:-"))
    sql = f"DELETE FROM EMPLOYEE WHERE E_ID = {E_ID};"
    root_.execute(sql)
    root.commit()
    print(".....RECORD DELETED.....")

def data_search():
    print("1.SEARCH BY EMPLOYEE ID\n2.SEARCH BY NAME\n3.SEARCH BY DESIGNATION")
    choicee = int(input("ENTER THE CHOICE(1-3):-"))
    if choicee == 1:
        E_ID = input("ENTER EMPLOYEE ID:-")
        sql = f"SELECT * FROM EMPLOYEE WHERE E_ID = {E_ID};"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["EMPLOYEE ID","NAME","AGE","SALARY","DESGNATION"]))
    elif choicee == 2:
        name = input("ENTER THE EMPLOYEE NAME:-")
        sql = f"SELECT * FROM EMPLOYEE WHERE NAME = {name};"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["EMPLOYEE ID","NAME","AGE","SALARY","DESGNATION"]))
    elif choicee == 3:
        desig = input("ENTER THE EMPLOYEE DESIGNATION:-")
        sql = f"SELECT * FROM EMPLOYEE WHERE DESIGNATION = {desig}"
        root_.execute(sql)
        records = root_.fetchall()
        print(tabulate(records, headers = ["EMPLOYEE ID","NAME","AGE","SALARY","DESGNATION"]))
    else:

        return

def data_display():
    sql = "SELECT * FROM EMPLOYEE;"
    root_.execute(sql)
    records = root_.fetchall()
    print(tabulate(records,headers = ["EMPLOYEE-ID", "NAME","AGE","SALARY","DESIGNATION"]))

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

