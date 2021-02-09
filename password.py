import time

Rule = ["Password should be of minimum of 8 letters and maximum of 20 letters.",
        "Should contain alphanumeric characters.",
        "Should have one symbol \"@#$*&%^\"."]

def split_char(data):
    data_new = []
    for x in data:
        data_new.append(x)
    return data_new

Number = split_char('0123456789')
Alphabates = split_char('abcdefghijklmnopqrstuvwxyz')
Symbol = split_char('@#$%^&*')


def Enter_password():
    for x in Rule:
        print(x)
    #Password = input("Enter password: ")
    #Password = split_char(Password.lower())
    check_box()

def check_box():
    password = input("Enter password: ")
    password = split_char(password.lower())
    three_check = []
    for x in password:
        if x in Alphabates:
            three_check.append(True)
            break        
    for x in password:
        if x in Number:
            three_check.append(True)
            break
    for x in password:
        if x in Symbol:
            three_check.append(True)
            break
    if len(password) < 8 or len(password) > 20 or len(three_check) < 3:
        print("Not a valid password.")
        print("Try again.")
        #Enter_password()
        check_box()
    else:
        print("***Valid Password***")
        print("Thanks for your interest.")
        time.sleep(4)
        exit()

Enter_password()