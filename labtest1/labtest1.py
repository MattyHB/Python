userInput = input("Enter some text: ")
charNum = len(userInput)
if userInput == "EAT":
    print('Eat what?')

lastChar = userInput[-1:]


def getLastChar(text:str) -> str:
    
    if text =='':
        return ''
    else:
        last = text[-1:]
        last = last.upper()
        return last

def getSecondWord(text:str) -> str:
    firstPos = 0 
    secPos = 0
    spaceCount = 0
    for i in text:
        if i == ' ':
            firstPos = i
            spaceCount += 1
            return firstPos
        else:
            return ''
        if i == ' ':
            secPos = 1
            spaceCount += 1
            return secPos
        else:
            return ''
    return text[firstPos:secPos]


i = 0
charCount = 0
for i in userInput:
    if i == "R":
        print("R found in position", charCount) 
        charCount += 1   

    elif "R" not in userInput:
        print("No R found")
    else:
        charCount += 1

print('You have entered', charNum ,'characters')
print('The last character you entered was:', lastChar)

assert getLastChar('bwoohahahahahaha') == 'A'
assert getLastChar('SKEWERED') == 'D'
assert getLastChar('') == ''
