import bottle
import lmc

The_HTML = '''<html>

<body>
    <h1>Little Man Computer</h1>
    <form>
        <pre>{0}
        </pre>
        <input type="submit" name="action" value="Step">
        <input type="submit" name="action" value="Run">
        <h2>Load Program</h2>
        <textarea name="program" rows="20" cols="30">Enter program here</textarea><br>
        Enter input here (comma-delimited numbers): <input type="text" name="inbox" value="2,3,4">
        <input type="submit" name="action" value="Load">
    </form>
</body>

</html>''' 

@bottle.route('/')
def welcome():
    reDump = lmc.dumpForWeb()

    if 'program' in bottle.request.params:
        finalProg = []
        program = bottle.request.params['program']
        if '\\n' in program:
            program = program.split('\\n')
        if '\\r' in program:
            program = program.split('\\r')
        if '\n' in program:
            program = program.split('\n')
        if '\r' in program:
            program = program.split('\r')
        #program = program.split('%0D%0A')

        for i in program:
            finalProg.append(i)
        print(finalProg)

    if 'inbox' in bottle.request.params:
        finalInbox = []
        inbox = bottle.request.params['inbox']
        #inbox = inbox.split('%2C')
        inbox = inbox.split(',')
        for i in inbox:
            i = int(i)
            finalInbox.append(i)
        print(finalInbox)
        

    if 'action' in bottle.request.params:
        action = bottle.request.params['action']
        if action == 'Step':
            lmc.step()
        elif action == 'Run':
            lmc.run()
        elif action == 'Load':
            lmc.load(finalProg, finalInbox)
    

    
    return The_HTML.format(reDump)



# Launch the BottlePy dev server
bottle.run(host='localhost', debug=True)
