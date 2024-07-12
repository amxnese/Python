import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()
db.execute("CREATE TABLE if not exists skills(name text ,progress integer, user_id integer)")
cr.execute("CREATE TABLE if not exists users (user_id integer , name text)")
cr.execute("insert into users (user_id,name) values(6871,'amine')")
cr.execute("insert into users (user_id,name) values(5746,'hicham')")
cr.execute("insert into users (user_id,name) values(7564,'youcef')")
db.commit()
db.close()


mylist = ["amine", "hisham","samy", "steve","najwa","mohamed"]
db = sqlite3.connect("new")
cr = db.cursor()
cr.execute("create table if not exists members (name_id integer,name text)")
for key, value in enumerate(mylist):
    cr.execute(f"insert into members (name_id,name) values({key+1},'{value}')")
cr.execute("select * from members")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchall())
print(cr.fetchmany(3))
db.commit()
db.close()
print(sqlite3.__doc__)


try:
    db = sqlite3.connect("new.db")
    print("connected to the database successfully")
    cr = db.cursor()
    cr.execute("create table if not exists members(name text,name_id integer)")
    ### cr.execute("insert into members(name,name_id) values ('steve',4)")
    db.commit()
    cr.execute("select * from members")
    result = cr.fetchall()
    print(result)
    print(f"you have {len(result)} rows in your table")
    for rows in result:
        print("showing data")
        print(f"username is ==> {rows[0]},and user's id is ==> {rows[1]}")
    db.close()
except sqlite3.Error as er:
    print(f"error reading data {er}")
finally:
    if db():
        db.close()
        print("database closed")

db = sqlite3.connect("new.db")
cr = db.cursor()
cr.execute("update members set name = 'clause' where name_id = 1")
cr.execute("delete from members where name_id = 4")
cr.execute("select * from members")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
db.commit()