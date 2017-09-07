name1 = input("Please enter the name of Player 1: ")
name2 = input("Please enter the name of Player 2: ")

# First Question
    #First Player
answer1_1 = input("How many stuffed animals do you own, " + name1 + "? ")
runningTotalP1 = int(answer1_1) * 3 + 5
print("> Your turtle moves", runningTotalP1, "steps. Total steps so far:" , runningTotalP1)
    #Second Player
answer1_2 = input("How many stuffed animals do you own, " + name2 + "? ")
runningTotalP2 = int(answer1_2) * 3 + 5
print("> Your turtle moves", runningTotalP2, "steps. Total steps so far:" , runningTotalP2)


# Second Question
    # First Player
answer2_1 = input(name1 + ", what is your favorite Cola? ")
if answer2_1 == str("Coke"):
    currentTotal = 10
elif answer2_1 == str("Pepsi"):
    currentTotal = 5
else:
    currentTotal = 3       
runningTotalP1 = runningTotalP1 + currentTotal
print("> Your turtle moves ", currentTotal, "steps. Total steps so far:" , runningTotalP1)
    #Second Player
answer2_2 = input(name2 + ", what is your favorite Cola? ")
if answer2_2 == str("Coke"):
    currentTotal = 10
elif answer2_2 == str("Pepsi"):
    currentTotal = 5
else:
    currentTotal = 3       
runningTotalP2 = runningTotalP2 + currentTotal
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)


# Third Question
    #First Player
answer3_1 = input(name1 + ", how many pairs of shoes did you bring to BJU? ")
if int(answer3_1) <= 2:
    currentTotal = 5
elif int(answer3_1) <= 5:
    currentTotal = 10
else:
    currentTotal = -5
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP1)

    #Second Player
answer3_2 = input(name2 + ",how many pairs of shoes did you bring to BJU? ")
if int(answer3_2) <= 2:
    currentTotal = 5
elif int(answer3_2) <= 5:
    currentTotal = 10
else:
    currentTotal = -5
print("> Your turtle moves", currentTotal, "steps. Total steps so far:" , runningTotalP2)




# Ending Statemnet
print(name1, "'s total score:", runningTotalP1)
print(name2, "'s total score:", runningTotalP2)

if int(runningTotalP1) > int(runningTotalP2):
    print("Congratulations, " + name1 + ", your turtle wins!")
else:
    print("Congratulations, " + name2 + ", your turtle wins!")
