import time
import webbrowser

totalBreaks = 3
breakCount = 0
time = time.ctime
num = 10

print("The program started at" , time)
while breakCount < totalBreaks:
    #time.sleep(num) This should be working...... Not quite sure why it isnt. The docs check out
    webbrowser.open("https://www.youtube.com/watch?v=2Z4m4lnjxkY")
    breakCount += 1