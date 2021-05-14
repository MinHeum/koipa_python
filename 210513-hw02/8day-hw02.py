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

# Mydb 연결, Man table 생성
c.execute('drop table if exists man')
c.execute('create table man(name char(10),age int)')
# insert 할 데이터 선언
lst_men = ["김연아/32","손흥민/30","이강인/21"]
for i in lst_men:
    line = i.split("/")
    # insert 쿼리문
    sql = """
        insert into man(name,age) values (%s,%s)"""
    c.execute(sql,(line[0],line[1]))
# select문으로 db에 작성되었는지 확인
c.execute("select * from man")
rows = c.fetchall()
for i in rows:
    print(i)

con.commit()
c.close()
con.close()