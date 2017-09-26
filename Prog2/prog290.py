ID = 0
def split(s: str, delim: str) -> (str, str):
    """Splits a string `s` into two parts, using `delim` as the separator character.

    Preconditions: None
    Postconditions:
      * If `delim` is present in `s`, returns 
         (portion of `s` before `delim`, portion of `s` after `delim`)
      * Otherwise, returns (`s`, '')
    """
    x = s.find(delim)
    if x == -1:
      return s, ''
    else:
        first = s[:x]
        second = s[x + 1:]
    
        return (first , second)

def test_split():
    assert split('100-200', '-') == ('100' , '200')
    assert split('os/360', '/') == ('os' , '360')
    assert split('no delimiter here', '-') == ('no delimiter here','')
    assert split('stuff ', '-') == ('stuff ','')

def isValidNum(num: str) -> bool:
    """ Takes string paramater and checks if it's a valid number"""
    decCount = 0
    for c in num:
        if c == '.':
            decCount += 1
        if c not in "1234567890.":
            return False
        if decCount > 1:
            return False
    return True

def test_isValidNum():
    assert isValidNum("12342024213") == True
    assert isValidNum("132213.12313") == True
    assert isValidNum("457427.25252.325") == False
    assert isValidNum("420w") == False

def extractData(coords: str) -> (str, float, float, float, float):    
    """Extracts data from a string. Seperates data into variables.

    Preconditions: None
    Postconditions:
      * Accurately partitioned variables from string.
    """

    (airplane, coordRemainder) = split(coords, ':')
    (xCoord, coordRemainder2) = split(coordRemainder, ',')
    (yCoord, coordRemainder3) = split(coordRemainder2,',')
    (heading, speed) = split(coordRemainder3,',')
    if isValidNum(xCoord) and isValidNum(yCoord) and isValidNum(heading) and isValidNum(speed)== True:
        xCoord = float(xCoord)
        xCoord = round(xCoord)
        yCoord = float(yCoord)
        yCoord = round(yCoord)
        return airplane,xCoord,yCoord,heading,speed
    else:
        return('ERROR',0,0,0,0)

def test_extractData():
    assert extractData('duck:100.15,25.2,0,550') == ('duck', 100, 25, '0', '550')
    assert extractData('airplane:500.44,250.13,180,235') == ('airplane' , 500 , 250 ,'180' ,'235')
    assert extractData('helicopter:34.9,400.2,90,300') == ('helicopter' , 35, 400, '90', '300')

def buildTableRow(airplane:str , xCoord:float , yCoord:float , heading:float , speed:float) -> (str):
    """This function is used to build the individal rows within the table. This will produce the HTML output
    needed to complete the final HTML page

    Preconditions: The data has already been split and ectracted by the split and extractData functions
    Postconditions:
      * Accurately accepts the extracted data and outputs a string of HTML code.
    """

    global ID
    ID += 1
    htmlRow = '''
    <tr>
    <td>{0} </td>
    <td><img src='{1}.png'></td>
    <td>({2},{3})
    </td>
    <td>{4}</td>
    <td>{5}</td>
    </tr>\n
        '''.format(ID, airplane, xCoord, yCoord, heading, speed)
        #0 = ID. 1 = pic 2 = xcoord. 3= Ycoord. 4= heading. 5 = speed
    return htmlRow

def makeHtml(rows):
    """This function is used to output a string of HTML code. Once it adds "rows" it will output HTML.

    Preconditions: The "rows" variable has a sting of HTML stored inside.
    Postconditions: 
      * Produces a fully functional HTML page stored in a string.
      * Accurately accepts the extracted data and outputs a string of HTML code.
    """
    
    return '''
        <html>
        <head>
            <style>
                table, td, th {
                    border: thin solid black;
                    margin: 0px;
                    padding: 10px;
                    border-collapse: collapse;
                    text-align: center;
                    border-color: white;            
                }
                th {   background-color: green;  }
                table {  display: table-inline;  }
                body {
                    font: arial;
                    background: black;
                    color: white;
                }
                h3 {
                    color: green;
                }
            </style>
        </head>
        <body>
            <div align='center'>
            <img src='atclogo.jpg'> 
            <h3>by Matthew Beals</h3>
            <table>
                <tr>
                    <th>Id</th><th>Type</th><th>Position</th><th>Heading</th>
                    <th>Speed</th>
                </tr>
        
    ''' + rows + '''

                </table>
                <br><br>
                </div>

        <p><i>Tips:
        <ul>
            <li> Right-click this page when viewing it in Chrome or Firefox and choose View Page Source to see the HTML you need to generate.</li>
            <li>Right-click each image and choose <b>"Save image as"</b> to download to your computer.
        </ul>
        </i></p>
        </body>
        </html>

            
        '''



def main():  
    """This function is the meat and potatoes of the code. Everything falls together in this function. It contains
    all the calculations needed and a loop to accept input until there is an empty string input by the user.

    Preconditions: All pervious functions are correct and ready to be used. 
    Postconditions: 
      * Will calculate everything in this program
      * Will use the string of HTML code from the makeHtml function to create a file.
      * If user inputs an empty string, I will create and print out an HTML document.
    """
    htmrows = ''
    
    while True:
        userInput = input("Enter Data: ")
        if userInput == '':
            break
        else:
            airplane, xCoord, yCoord, heading, speed = extractData(userInput)
            if airplane == 'ERROR':
                print('** WARNING: Invalid data detected.')
            else:    
                row = buildTableRow(airplane, xCoord, yCoord, heading, speed)
                htmrows += row 
            
    outFile = open("atc.html", "w")
    outFile.write(makeHtml(htmrows))
    outFile.close()

    print("Generating File...")


if __name__ == "__main__":
    main()   