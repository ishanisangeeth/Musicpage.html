names={"add":"password!", "Admin2":"12534", "Alia":"789890"}
username=(input("enter username" ))
password=(input("enter password" ))
findpassword=names.get(username,"login succesful")
if findpassword==password:
    print("login succeful")
else:
    print("login succesful")
    print("do you want to signup")
    login=(input("type yes or no"))
    if login=="yes":
        print("continue")
        names[username]=password
        print("loged in")
    if login=="no":
        print("try again next time")

