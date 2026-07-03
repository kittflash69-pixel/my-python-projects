# නමෝ බුද්දාය
password = "nethmika1234"
attempts = 0
print("Hellow")

while attempts < 3:

    x = input("Enter Your User Name:").lower().strip()
    if x == "":
        print("Sorry You must enter User Name")

    elif x == "nethmika1234":
        print("Your log in is done")
        break
    else:
        attempts += 1
        if attempts < 3:
            print(f"its wrong ,now you only have {3-attempts}")
        else:
            print("sorrt your acc is locked")
