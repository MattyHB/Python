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
    
    if 'action' in bottle.request.params:
        action = bottle.request.params['action']
        if action == 'Step':
            lmc.step()
        elif action == 'Run':
            lmc.run()
        elif action == 'Load':
            errors = lmc.loadAssembly(bottle.request.params['program'], bottle.request.params['inbox'])


            
    return The_HTML.format(lmc.dumpForWeb())
    
# Launch the BottlePy dev server
bottle.run(host='localhost', debug=True)
