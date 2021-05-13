import sqlite3 as s

con = s.connect('adb')
c = con.cursor()

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu, price)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')

con.commit()
c.close()
con.close()