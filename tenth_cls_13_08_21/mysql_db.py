from mysql import connector

# create database
try:
    conn = connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    sql = "CREATE DATABASE student"
    cursor.execute(sql)
    print("student database created")
    cursor.close()
    conn.close()
except Exception as e:
    print(e, " database already exists")

# create table database

try:
    conn = connector.connect(host="localhost", user="root", password="", database='student')
    cursor = conn.cursor()
    sql = "CREATE TABLE stu_info(id integer primary key auto_increment," \
          " stu_name varchar(100), stu_dept varchar(50) null )"
    cursor.execute(sql)
    print("Table created successfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

# insert data into table

try:
    conn = connector.connect(host="localhost", user="root", password="", database='student')
    cursor = conn.cursor()
    sql = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'Shamim', 'IT')"
    sql2 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'Subin', 'CSE')"
    sql3 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'Rasel', 'BBA')"
    sql4 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'tarek', 'SS')"
    sql5 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'Mohin', 'MBA')"
    cursor.execute(sql)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    # conn.commit()
    print("value inserted:")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

# fetch the value

try:
    conn = connector.connect(host="localhost", user="root", password="", database='student')
    cursor = conn.cursor()
    sql = "SELECT * FROM stu_info"
    cursor.execute(sql)
    res = cursor.fetchall()
    for i in res:
        print(i, end="\n")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

# update the value

try:
    conn = connector.connect(host="localhost", user="root", password="", database='student')
    cursor = conn.cursor()
    sql = "UPDATE stu_info SET stu_dept='BBS' WHERE id = 8"
    cursor.execute(sql)
    conn.commit()
    fetch = "SELECT * FROM stu_info"
    cursor.execute(fetch)
    res = cursor.fetchall()
    for i in res:
        print(i, end="\n")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

# delete the values
try:
    conn = connector.connect(host="localhost", user="root", password="", database='student')
    cursor = conn.cursor()
    sql = "DELETE FROM stu_info WHERE id = 2"
    cursor.execute(sql)
    conn.commit()
    fetch = "SELECT * FROM stu_info"
    cursor.execute(fetch)
    res = cursor.fetchall()
    for i in res:
        print(i, end="\n")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)
