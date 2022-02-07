import mysql.connector as sqlcon

db = sqlcon.connect(host = "localhost", user = "root", passwd = "system", database = 'samp')

cur = db.cursor()

cur.execute("update student set mark = 89 where sname = 'Hari'")
cur.execute("select * from student")

for i in cur:
	print(i)

cur.close()
db.commit()



# SQL Statements

'''

create database samp;

show databases;
use samp;
show tables;
create table student(roll int, sname varchar(30), mark int);
desc student;

insert into student values(101, 'Hari', 87);
insert into student values(102, 'Satheesh', 92);
insert into student values(103, 'Siva', 77);

select * from student;

set SQL_SAFE_UPDATES = 1;

commit;

'''
