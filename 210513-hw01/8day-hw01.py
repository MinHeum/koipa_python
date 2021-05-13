import sqlite3 as s

con = s.connect('adb')
c = con.cursor()
c.execute('drop table if exists movie')
c.execute('create table movie(title,director,actor,audience)')
with open('m.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split("|")
        title, director, actor, audience = line
        c.execute('insert into movie values(?,?,?,?)', [title,director,actor,audience])
for row in c.execute('select * from movie'):
    print(row)

# 5) movie 테이블에 명량|김한민|최민식|1761 삽입하기
c.execute('insert into movie values(?,?,?,?)', "명량|김한민|최민식|1761".split("|"))
print("========================================")
for row in c.execute('select * from movie'):
    print(row)

# 5) 도둑들의 배우를 김혜수로 변경
c.execute('update movie set actor = "김혜수" where "title" = "도둑들"')
print("========================================")
for row in c.execute('select * from movie'):
    print(row)

# 5) 국제시장을 삭제
c.execute('delete from movie where title = "국제시장"')
print("========================================")
for row in c.execute('select * from movie'):
    print(row)

# 6) Man(name, age)테이블 생성
c.execute('drop table if exists man')
c.execute('create table man(name, age)')
lst_men = ["김연아/32","손흥민/30","이강인/21"]
for i in lst_men:
    c.execute('insert into man values(?,?)', (i.split("/")))
print("========================================")
for row in c.execute('select * from man'):
    print(row)

# 7) movie 테이블 관객순으로 출력
print("========================================")
for row in c.execute('select * from movie order by audience desc'):
    print(row)

con.commit()
c.close()
con.close()