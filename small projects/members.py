import sqlite3
members = ["amine","samuel","mohamed","adam"]
name = input("please insert your name:  ")
if name in members:
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute("select * from user")
    print(f"hello {name} welcome to the database of yours")
    print(cr.fetchall())
else:
    raise NameError("the name you added has not been found")
command_list = ["a","u","d","s","q"]
input_var ='''
what command do you want to apply
"a" ==> add user
"u" ==> update user
"d" ==> delete user
"s" ==> show users
"q" ==> quit database
Choose an option:
'''
def cac():
    db.commit()
    cr.close()
user_input = input(f"{input_var} ==>  ")
def add_user():
    name = input(f"enter the new user's name:   ").lower().strip()
    sk = input("enter the new user's skill:   ").lower().strip()
    nid = input("enter the new user's id:   ")
    cr.execute(f"select name_id from user  where name_id = '{nid}'")
    rslt = cr.fetchone()
    if rslt == None:
        cr.execute(f"insert into user(name,skill,name_id) values ('{name}','{sk}',{nid})")
        print("user added succesfully")
    else:
        cr.execute(f"select name from user where name_id = {nid}")
        aun = cr.fetchone()
        stts = input(f'''
        the given id has been already used for {aun}
        would you like to override username?
        y ===> Yes
        n ===> No
        ''').lower()
        if stts == "n":
            print("database closed")
            cac()
        elif stts == "y":
            cr.execute(f"update user set name = '{name}' where name_id = {nid}")
            cr.execute(f"update user set skill = '{sk}' where name_id = {nid}")
            print("username and skill updated successfully")
            cac()
def update_user():
    status = input('''
    what are you updating:   
    n ==>  name
    s ==>  skill
    i ==>  name's id
    choose an option:   
    ''')
    if status == "n":
        id = input("enter the id of the name you want to update:   ")
        nm = input("inser updated name:   ").lower().strip()
        cr.execute(f"update user set name = '{nm}' where name_id = {id}")
        print("name updated successfully")
        cac()
    elif status == "s":
        id = input("enter the id of the skill you want to update:   ")
        ns = input("insert updated skill:   ").lower().strip()
        cr.execute(f"update user set skill = '{ns}' where name_id = {id}")
        print("skill updated successfully")
        cac()
    elif status == "i":
        name = input("enter the username that you want to change his id    :").lower().strip()
        skill = input("enter the skill of the username that you want to change his id:   ").lower().strip()
        new_id = input("insert updated id:   ")
        cr.execute(f"update user set name_id = {new_id} where name = '{name}' and skill = '{skill}'")
        print("name_id updated successfully")
        cac()
    else:
        raise NameError("the input given is invalid")
def delete_user():
    dname = input(f"enter the name you want to delete:   ")
    nid = input("enter the user's id:   ")
    cr.execute(f"delete from user where name = '{dname}' and name_id = {nid}")
    print("user deleted succesfully")
def show_user():
    cr.execute("select * from user")
    users = (cr.fetchall())
    print(f"there are {len(users)} users stored in the database")
    for i in users:
        print(f"username is ({i[0]}), user skill is ==> ({i[1]}), and user id is ({i[2]})")
if user_input in command_list:
    if user_input == "a":
        add_user()
        cac()
    elif user_input == "u":
        update_user()
        cac()
    elif user_input == "d":
        delete_user()
        cac()
    elif user_input == "s":
        show_user()
        cac()
    else:
        print("closed database")
        cac()
else:
    print(f"command '{user_input}' not found")