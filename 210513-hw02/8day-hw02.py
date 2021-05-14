import sqlite3 as s
import pymysql as my

DB_PASSWORD = ""
with open('DB_PASSWORD', 'r') as f:
    DB_PASSWORD = f.readline()

con = my.connect(
    user='root',
    password=DB_PASSWORD,
    host='127.0.0.1',
    db='bdb',
    charset='utf8'
)

c = con.cursor()
c.execute('drop table if exists movie')
c.execute('create table movie(title char(20),actor char(10),audience int)')
with open('m.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split("|")
        title, actor, audience = line
        sql = """
        insert into movie(title,actor,audience) values (%s,%s,%s)"""
        c.execute(sql,(title,actor,audience))

# 명량|최민식|1761  insert하시오. 
c.execute('insert into movie(title,actor,audience) values(%s,%s,%s)',("명량","최민식","1761"))
# 도둑들의 배우를 김혜수로 바꾸시오. update
c.execute('update movie set actor = "김혜수" where title = "도둑들"')
# 광해를 삭제하시오. delete
c.execute('delete from movie where title = "광해"')


con.commit()
c.close()
con.close()