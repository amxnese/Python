tries = 4
mainPassword = "amine123"
givenPassword = input("enter your password:   ")
while not givenPassword == mainPassword:
    tries -= 1
    if tries == 1:
        print("careful, this is your last chance")
        givenPassword = input("enter your password:   ")
    elif tries > 0:
        print(f"wrong password, {tries} attempts left")
        givenPassword = input("enter your password:   ")
    elif tries == 0:
        print("you're out of attempts")
        break
else:
    print("correct password")