import bottle
import random
import traceback

class SVGDrawing:
    def __init__(self, width: int,height: int):
        self.width = width
        self.height = height
        self.svgdata = []
    
    def drawRect(self, x: int, y:int, width: int, height:int , color: str):
        self.svgdata.append("<rect x='{0}' y='{1}' width='{2}' height='{3}' fill='{4}' />".format(x, y, width, height, color))
    
    def drawLine(self, startx, starty, endx, endy, color):
        self.svgdata.append("<line x1='{0}' y1='{1}' x2='{2}' y2='{3}' stroke='{4}' />".format(startx, starty, endx, endy, color))

    def drawText(self, x, y, text):  
        self.svgdata.append("<text x='{0}' y='{1}' font-family='Verdana' font-size='10' stroke='white'>{2}</text>".format(x, y, text))

    def drawImage(self, x, y, image, width, height ):  
        self.svgdata.append("<image x='{0}' y='{1}' xlink:href='images/{2}' width='{3}' height='{4}' />".format(x, y, image, width, height))

    def generateDrawing(self):
        string = ''
        for i in self.svgdata:
            string += i + '\n'
        
        return string

WIDTH=700
HEIGHT=700

@bottle.route('/')
def welcome():  
    d = SVGDrawing(700,700)
    d.drawRect(0,0,700,700, 'black')
    
    for x in range(0, WIDTH+1, 100):
        d.drawLine(x,0,x,WIDTH,'green')

    for y in range(0, HEIGHT+1, 100):
        d.drawLine(0, y, WIDTH, y, 'green')

    d.drawImage(20,30,'duck.png',50,50)
    d.drawText(10,20, 'Some text here')
    drawing = d.generateDrawing()
    return HTML_PAGE.format(WIDTH, HEIGHT, drawing)

@bottle.route('/<filename:path>')
def send_static(filename):
    """Serve up images and sounds."""
    return bottle.static_file(filename, root='.')


HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

<svg width="{0}" height="{1}">
  {2}
</svg>

</body>
</html>
"""

if __name__ == '__main__':

    # Launch the BottlePy dev server
    import wsgiref.simple_server
    wsgiref.simple_server.WSGIServer.allow_reuse_address = 0
    bottle.run(host="localhost", port=8080, debug=True)
    