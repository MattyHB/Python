# -----------------------------------------------------------
# File:   icebreaker.py 
# Author: Matt Beals  User ID: Mbeal872   Class: CPS 110
# Desc:   This program is intended to serve as an icebreaker game for two roommates at BJU
# ----------------------------------------------------------- 
name1 = input("Enter the name of Player 1: ")
name2 = input("Enter the name of Player 2: ")
print()

# First Question
    #First Player
answer1_1 = input(name1 + ", how many stuffed animals do you have? ")
runningTotalP1 = int(answer1_1) * 3 + 5
print("> Your turtle moves", runningTotalP1, "steps. Total steps so far:" , runningTotalP1)
print()

   #Second Player
answer1_2 = input(name2 + ", how many stuffed animals do you have? ")
runningTotalP2 = int(answer1_2) * 3 + 5
print("> Your turtle moves", runningTotalP2, "steps. Total steps so far:" , runningTotalP2)
print()


# Second Question
    # First Player
answer2_1 = input(name1 + ", what is your favorite Cola? ")
if answer2_1 == "coke":
    currentTotal = 10
elif answer2_1 == "pepsi":
    currentTotal = 5
else:
    currentTotal = 3       
runningTotalP1 = runningTotalP1 + currentTotal
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP1)
print()

#Second Player
answer2_2 = input(name2 + ", what is your favorite Cola? ")
if answer2_2 == "coke":
    currentTotal = 10
elif answer2_2 == "pepsi":
    currentTotal = 5
else:
    currentTotal = 3       
runningTotalP2 = runningTotalP2 + currentTotal
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)
print()



# Third Question
    #First Player
answer3_1 = input(name1 + ", how many pairs of shoes did you bring to BJU? ")
if int(answer3_1) <= 2:
    currentTotal = 5
elif int(answer3_1) <= 5:
    currentTotal = 10
else:
    currentTotal = -5
runningTotalP1 = currentTotal + runningTotalP1
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP1)
print()


    #Second Player
answer3_2 = input(name2 + ", how many pairs of shoes did you bring to BJU? ")
if int(answer3_2) <= 2:
    currentTotal = 5
elif int(answer3_2) <= 5:
    currentTotal = 10
else:
    currentTotal = -5
runningTotalP2 = currentTotal + runningTotalP2
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)
print()


# 90 version 
# Fourth question
    # First Player
answer4_1 = input(name1 + ", how many Facebook friends do you have? ")
friendNum1 = int(answer4_1)
if friendNum1 <= 500:
    currentTotal = friendNum1 // 100 * 10
elif friendNum1 > 500:
    currentTotal = friendNum1 // 500 * 5 + 25
runningTotalP1 = currentTotal + runningTotalP1
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP1)
print()


    # Second Player
answer4_2 = input(name2 + ", how many Facebook friends do you have? ")
friendNum2 = int(answer4_2)
if friendNum2 <= 500:
    currentTotal = friendNum2 // 100 * 10
elif friendNum2 > 500:
    currentTotal = friendNum2 // 500 * 5 + 25
runningTotalP2 = currentTotal + runningTotalP2
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)
print()



# 100 Version
# Fifth Question
    # First Player
validEntry1 = False

while validEntry1 == False:
    confirm = input(name1 + ", what is your favorite OS? ")
    if confirm == "Windows":
        validEntry1 = True
        currentTotal = 10
    elif confirm == "iOS":
        validEntry1 = True
        currentTotal = 5
    else:
        print("I’m sorry, but you must choose Windows or iOS.")
runningTotalP1 = currentTotal + runningTotalP1
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP1)
print()



    # Second Player
validEntry2 = False

while validEntry2 == False:
    confirm = input(name2 + ", what is your favorite OS? ")
    if confirm == "Windows":
        validEntry2 = True
        currentTotal = 10
    elif confirm == "iOS":
        validEntry2 = True
        currentTotal = 5
    else:
        print("I’m sorry, but you must choose Windows or iOS..")
runningTotalP2 = currentTotal + runningTotalP2
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)
print()


# Ending Statemnet
print(name1, "'s total score:", runningTotalP1)
print(name2, "'s total score:", runningTotalP2)
print()


if int(runningTotalP1) > int(runningTotalP2):
    print("Congratulations, " + name1 + ", your turtle wins!")
else:
    print("Congratulations, " + name2 + ", your turtle wins!")