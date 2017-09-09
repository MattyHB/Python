validEntry2 = False
name2 = "Matt"
while validEntry2 == False:
    confirm = input(name2 + ", what is your favorite OS? ")
    if confirm == "Windows":
        validEntry2 = True
        currentTotal = 10
    elif confirm == "iOS":
        validEntry2 = True
        currentTotal = 5
    else:
        print("Invalid entry.")
#runningTotalP2 = currentTotal + runningTotalP2
#print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2
