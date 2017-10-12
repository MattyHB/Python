# lmc.py
# An implementation of a modified Little Man Computer
# https://en.wikipedia.org/wiki/Little_man_computer

# Global variables for LMC components
memory = [0] * 100
pc = 0
accum = 0
inbox = []
outbox = []
running = True  # Set to False when HLT is executed

# Instruction numbers
HLT = 0
ADD = 1
SUB = 2
STA = 3
LDA = 4
BRA = 5
BRZ = 6
INP = 7
OUT = 8
names = ["HLT", "ADD", "SUB", "STA", 'LDA', "BRA", "BRZ", "INP", "OUT"]


# ---------------- LMC Component Interfaces ------------------

def readMem(addr: int) -> int:
    """Returns value at address `addr` in memory, or 0 if `addr` is out of range"""
    if 0 <= addr < len(memory):
        return memory[addr]
    else:
        return 0

def writeMem(addr: int, val: int):
    """Writes `val` to memory cell at address `addr`"""
    if 0 <= addr < len(memory) and 0 <= val <= 999:
        memory[addr] = val

def readAccum():
    """Returns value of accumulator"""
    return accum

def writeAccum(val: int):
    """Writes `val` to accumulator, if 0 <= `val` <= 999"""
    global accum
    if 0 <= val <= 999:
        accum = val

def readPC():
    """Returns current program counter value"""
    return pc

def writePC(val: int):
    """Writes `val` to program counter, if 0 <= `val` <= 999"""
    global pc
    if 0 <= val < len(memory):
        pc = val

def readInbox():
    """Removes and returns first number from inbox. If inbox is empty, returns 0."""
    global inbox
    if len(inbox) == 0:
        return 0
    return inbox.pop(0)

def writeOutbox(val: int):
    """Places `val` at end of outbox"""
    outbox.append(val)

# ------------ Fetch / Decode / Execute Functions ------------

def fetch():
    """Fetches and returns next instruction indicated by PC. Increments PC."""
    pcval = readPC()
    instr = readMem(pcval)
    writePC(pcval + 1)
    return instr

def decode(instr: int) -> (int, int):
    """Decodes instruction `instr`, returning its (opcode, operand)"""
    return (instr // 100, instr % 100)

def execute(opcode: int, operand: int):
    """Executes instruction corresponding to `opcode`, using `operand` if needed"""
    global running
    if opcode == OUT:
        writeOutbox(readAccum())
    elif opcode == LDA:
        writeAccum(readMem(operand))
    elif opcode == HLT:
        running = False
    elif opcode == ADD:
        writeAccum(readAccum() + readMem(operand))
    elif opcode == SUB:
        writeAccum(readAccum() - readMem(operand))
    elif opcode == STA:
        writeMem(operand, readAccum())
    elif opcode == BRA:
        writePC(operand)
    elif opcode == BRZ:
        if readAccum() == 0:
            writePC(operand)
    elif opcode == INP:
        writeAccum(readInbox())

def step():
    """Performs one fetch-decode-execute step"""
    instr = fetch()
    
    (opcode, operand) = decode(instr)
    execute(opcode, operand)

def run():
    """Performs fetch-decode-execute steps until `running` is False"""
    while running:
        step()

# ----------------- Simulator setup ----------------

def reset():
    """Resets all computer components to their initial state"""
    global pc, memory, accum, inbox, outbox, running
    pc = 0
    memory = [0] * 100
    accum = 0
    inbox = []
    outbox = []
    running = True

def load(program: list, indata: list):
    """Resets computer, loads memory with `program`, and sets inbox to `indata`"""
    global inbox
    reset()
    for i in range(len(program)):
        writeMem(i, program[i])
    inbox = indata
    print()

# ---------------- Simulator "display" ----------------------

def dump():
    """ Displays the state of memory/CPU"""
    print()
    for i in range(0, 10):
        row = ''
        for j in range(0, 10):
            row += "{index:2}[{loc:<3}] ".format(index= i * 10 + j, loc = readMem(i * 10 + j))
        
        print(row)
    thirdLast = ' ' * 32 + "PC[{P:<2}] ACC[{A:<3}] {toa}".format(P = readPC(), A = readAccum(), toa = toAssembly(readMem(pc)))
    print(thirdLast)
    print()
    secondLast = "In Box: " + str(inbox)
    print(secondLast)
    last= "Out Box: " + str(outbox)
    print(last)
    print()
    dumpForWeb()

def dumpForWeb():
    '''Converts the contents of dump to a string'''
    string = ''
    for i in range(0, 10):
        row = ''
        for j in range(0, 10):
            row += "{index:2}[{loc:<3}] ".format(index= i * 10 + j, loc = readMem(i * 10 + j))
        
        string+= row + '\n'
    thirdLast = ' ' * 32 + "PC[{P:<2}] ACC[{A:<3}] {toa}".format(P = readPC(), A = readAccum(), toa = toAssembly(readMem(pc)))
    string += thirdLast
    string += '\n'
    secondLast = "In Box: " + str(inbox)
    string += secondLast + '\n'
    last= "Out Box: " + str(outbox)
    string += last
    string += '\n'
    
    return string

def toAssembly(instr: int) -> str:
    """ Returns assembly language translation of machine language instruction `instr`"""
    opcode, operand = decode(instr)
    final = names[opcode]
    if opcode > 0 and opcode < 7:
        final += ' ' + str(operand) 
    return final

def encode(asm: str) -> int:
    '''Encodes one assembly language instruction into a machine language instruction
            Precondition: None
            Postconditions: Returns machine language code in the form of an integer.
    '''

    asm = asm.rstrip()
    if ' ' not in asm:
        for num, name in enumerate(names):
            if asm == name:
                num = num * 100
                return num
        return -1
    else:
        opcode, operand = asm.split(" ")
        operand = int(operand)
        
        if opcode == 'DAT':
            return operand
        elif opcode not in names:
            return -1
        for num, name in enumerate(names):
            if opcode == name:
                converted = num * 100
        return converted + operand

def assemble(program:str)-> (list, list):
    ''' Takes a long string of machine language code and transforms it into an assembly language list of instructions with a second list to catch all errors.
        Preconditions: None
        Postconditions: Returns two lists, one assembly code and one for errors.
    '''
    codes = []
    errors = []
    for line in program.split('\n'):
        if line.find('//') > -1:
            line = line[0:line.find('//')]
        if line == '':
            continue
        if encode(line) == -1:
            errors.append(line)
        else:
            codes.append(encode(line))
    return codes , errors 

def disassemble(start: int, end: int):
    """Displays assembly language listing of memory contents `start` to `end`"""
    for addr in range(start, end + 1):
        print(str(addr).rjust(2) + ": " + toAssembly(readMem(addr)))
    print()

def loadAssembly(program: str, indata: str):
    '''Loads `program` into the `memory` and `indata` into the`inbox`
            Preconditions: None
            Postconditions: Program has been loaded into 'memory`
                            `indata` has been moved into the `inbox`'''
    (loaded, errors) = assemble(program)
    
    data = []
    for i in indata.split(","):
        data.append(int(i))
    if errors == []:    
        load(loaded, data)
    else:
        print('The following instructions failed to assemble:')
        for i in errors:
            print(i)
        

# ----------- Define shortcut names for interactive use

def sd():
    step()
    dump()

s = step
d = dump
r = run       

# ----------------- Unit Tests ------------------------

def test_mem():
    reset()
    assert memory == [0] * 100
    writeMem(1, 5)
    assert readMem(1) == 5

    reset()
    writeMem(-1, 5)
    assert memory == [0] * 100

    writeMem(1, 1000)
    assert memory == [0] * 100

def test_LDA():
    reset()
    writeMem(3, 50)
    execute(LDA, 3)
    assert readAccum() == 50

def test_OUT():
    reset()
    writeAccum(3)
    execute(OUT, 0)
    assert outbox == [3]

def test_toAssembly():
    assert toAssembly(189) == "ADD 89"
    assert toAssembly(232) == "SUB 32"
    assert toAssembly(323) == "STA 23"
    assert toAssembly(401) == "LDA 1"
    assert toAssembly(522) == "BRA 22"
    assert toAssembly(643) == 'BRZ 43'
    assert toAssembly(701) == 'INP'
    assert toAssembly(802) == 'OUT'
    assert toAssembly(000) == 'HLT'

def test_encode():
    assert encode('DAT 8') == 8
    assert encode('HLT') == 0
    assert encode('ADD 2') == 102
    assert encode('SUB 3') == 203
    assert encode('STA 4') == 304
    assert encode('LDA 5') == 405
    assert encode('BRA 6') == 506
    assert encode('BRZ 7') == 607
    assert encode('INP') == 700
    assert encode('OUT') == 800
    

def test_exe():
    reset()
    load([2,3,4,5,6,7,8,9,0,1], [])
    execute(ADD, 0)
    assert readAccum() == 2
    execute(ADD, 3)
    assert readAccum() == 7
    execute(SUB, 4)
    assert readAccum() == 1
    execute(STA, 8)
    assert readMem(8) == 1
    execute(BRA, 4)
    assert readPC() == 4
    execute(BRZ, 9)
    assert readAccum() == 1
    writeAccum(0)
    execute(BRZ, 4)
    assert readPC() == 4
    reset()
    load([1,2,3,4,5], [2, 3, 4])
    execute(INP, 0)
    assert readAccum() == 2
    assert inbox == [3, 4]

def test_readInbox():
    global inbox
    inbox = [1,2,3,4,5,6,7,8]
    assert readInbox() == 1
    assert inbox == [2,3,4,5,6,7,8]
    assert readInbox() == 2
    assert inbox == [3,4,5,6,7,8]

# Multiply two numbers
multiply = """
INP
STA 99
INP
STA 98
LDA 99
BRZ 13
LDA 97
ADD 98
STA 97
LDA 99
SUB 16
STA 99
BRA 4
LDA 97
OUT
HLT
DAT 1
"""

if __name__ == "__main__":
    reset()
    
    