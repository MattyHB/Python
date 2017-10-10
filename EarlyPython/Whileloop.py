validEntry = False

while validEntry == False:
    confirm = input("What is your favorite OS? ")
    if confirm == "Windows":
        validEntry = True
    elif confirm == "iOS":
        validEntry = True
    else:
        print("Invalid entry.")

print(confirm)