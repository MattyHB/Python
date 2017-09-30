#def getSecondWord(text:str) -> str:
firstPos = 0 
secPos = 0
letterCount = 0
spaceCount = 0
text = "My name is Matt"
for i in text:
    if i == ' ':
        firstPos = len(text[:letterCount])
        spaceCount += 1
        letterCount +=1
        print(firstPos)
        #return firstPos
    elif spaceCount == 1 and i == ' ':
        secPos = len(text[:letterCount])
        spaceCount += 1
        letterCount += 1
        print(secPos)
        #return secPos
#    else:
        #return ''
plin = text[firstPos:secPos]
print(plin)
#return text[firstPos:secPos]






# def test_getSec():
    #assert getSecondWord('A cat ate my hat') == 'cat'
    #assert getSecondWord('Run, Spot!') == 'Spot!'
    #assert getSecondWord('Run!') ==''
    #assert getSecondWord('') == ''
