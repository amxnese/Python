
admins = ["Amine","Khalil","Sadek","Rafik","Mahmoud"]
name = input("please enter your name:   ").capitalize().strip()
if name in admins:
    print(f"Welcome back {name}")
    option = input("would you like to update (u) or delete (d) your name?   ").lower().strip()
    while not option == "d" and not option == "u":
        option = input("invalid option, Please insert 'u' for update or 'd' for delete:  ").lower().strip()
    if option == "d":
        admins.remove(name)
        print(f"({name}) has been deleted")
    elif option == "u":
        NewName = input("please enter your new name:  ").capitalize().strip()
        admins[admins.index(name)] = NewName
        print("name updated successfully")
else:
    print(f"hello {name} this is your first time here")
    status = input("would you like to be an admin? y for yes and n for no:    ").strip().lower()
    while not status == "y" and not status == "n":
        status = input("invalid option, please insert y for yes or n for no:    ").lower().strip()
    if status == "y":
        admins.append(name)
        print("you are an admin now")
    elif status == "n":
        print("you will be signed in as a guest ")