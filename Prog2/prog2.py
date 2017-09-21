def main():
    #does all the things

if __name__ == "__main__":
    main()



def extractData(coords: str) -> (str, float, float, float, float)
    




# For duck, ID 1, starting at (100,25) heading 0, speed 250.
#<tr>
#<td>1 </td>
#<td><img src='duck.png'></td>
#<td>(100,25)
#</td>
#<td>0</td>
#<td>550</td>
#</tr>



htmlPage = '''<html>
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
  
    {0}

        </table>
        <br><br>
        </div>

    <p><i>Tips:
    <ul>
    li> Right-click this page when viewing it in Chrome or Firefox and choose View Page Source to see the HTML you need to generate.</li>
    <li>Right-click each image and choose <b>"Save image as"</b> to download to your computer.
    </ul>
    </i></p>
    </body>
    </html>