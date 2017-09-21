# Generates a basic bar graph

numItems = int(input("How many items? "))

bars = ""
for i in range(1, numItems + 1):
    # 1. Get input
    line = input("Enter quantity and item description separated by comma:")
    qty = int("42") # ???
    descr = "wat"   # ???

    bars += "<img src='green.png' height='50' width='{0}'>{1}<br>\n".format(qty * 2, descr)

# Assemble HTML page into one string

htmlPage = '''<html>
<body>
<h1>Bar Graph Example</h1>
    {0}
</body>
</html>'''.format(bars)

# Write HTML to file named output.html

outFile = open("output.html", "w")
outFile.write(htmlPage)
outFile.close()

print("Output saved to output.html")