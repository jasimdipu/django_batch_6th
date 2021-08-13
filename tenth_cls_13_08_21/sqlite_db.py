import sqlite3

try:
    conn = sqlite3.connect(database='employee')
    cursor = conn.cursor()
    sql = "CREATE DATABASE employee"
    cursor.execute(sql)
    print("employee database created")
    cursor.close()
    conn.close()
except Exception as e:
    print(e, " database already exists")

try:
    conn = sqlite3.connect(database='student')
    cursor = conn.cursor()
    sql = "CREATE TABLE stu_info(id integer primary key," \
          " stu_name text, stu_dept text)"
    cursor.execute(sql)
    print("Table created successfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

try:
    conn = sqlite3.connect(database='student')
    cursor = conn.cursor()
    sql = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (0, 'Shamim', 'IT')"
    sql2 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (1, 'Subin', 'CSE')"
    sql3 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (2, 'Rasel', 'BBA')"
    sql4 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (3, 'tarek', 'SS')"
    sql5 = "INSERT INTO stu_info(id, stu_name, stu_dept ) values (4, 'Mohin', 'MBA')"
    cursor.execute(sql)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    conn.commit()
    print("value inserted:")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

try:
    conn = sqlite3.connect(database='student')
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
