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
    xCoord = float(xCoord)
    xCoord = round(xCoord)
    yCoord = float(yCoord)
    yCoord = round(yCoord)
    return airplane,xCoord,yCoord,heading,speed

def buildTableRow(airplane:str , xCoord:float , yCoord:float , heading:float , speed:float) -> (str):
    """This function is used to build the individal rows within the table. This will produce the HTML output
    needed to complete the final HTML page

    Preconditions: The data has already been split and ectracted by the split and extractData functions
    Postconditions:
      * Accurately accepts the extracted data and outputs a string of HTML code.
    """
    pic = 0
    global ID
    ID += 1
    if airplane == 'airplane':
        pic = "img src='airplane.png'"
    elif airplane == "duck":
        pic = "img src='duck.png'"
    elif airplane == 'helicopter':
        pic = "img src='helicopter.png'"
    htmlRow = '''
        <tr>
        <td>{0} </td>
        <td><{1}></td>
        <td>({2},{3})
        </td>
        <td>{4}</td>
        <td>{5}</td>
        </tr>\n
        '''.format(ID, pic, xCoord, yCoord, heading, speed)
        #0 = ID. 1 = pic 2 = xcoord. 3= Ycoord. 4= heading. 5 = speed
    return htmlRow


def makeHtml(rows):
    """This function is used to output a string of HTML code. Once it adds "rows" it will output HTML.

    Preconditions: The "rows" variable has a sting of HTML stored inside.
    Postconditions: 
      * Produces a fully functional HTML page stored in a string.
      * Accurately accepts the extracted data and outputs a string of HTML code.
    """
    
    return '''<html>
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
                </tr>''' + rows + '''
    
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
        </html>'''





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
            row = buildTableRow(airplane, xCoord, yCoord, heading, speed)
            htmrows += row 


    outFile = open("atc.html", "w")
    outFile.write(makeHtml(htmrows))
    outFile.close()

    print("Generating File...")


if __name__ == "__main__":
    main()   