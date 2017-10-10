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

def readMem(addr: list):
    """Returns value at address `addr` in memory, or 0 if `addr` is out of range"""
    if 0 <= addr < len(memory):
        return memory[addr]
    else:
        return 0

def writeMem(addr: int, val: list):
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


def toAssembly(instr: int) -> str:
    """ Returns assembly language translation of machine language instruction `instr`"""
    opcode, operand = decode(instr)
    final = names[opcode]
    if opcode > 0 and opcode < 7:
        final += ' ' + str(operand) 
    return final

def encode(asm: str) -> int:
    #
    #Write some documentations











    if " " in asm:
        opcode, operand = asm.split(" ")
        
        if opcode == 'DAT':
            return int(operand)
        if opcode not in names:
            return -1
        opcode = names.index(opcode)
        opcode = int(opcode) * 100
        final = opcode + int(operand)
    else:
        if asm not in names:
            return -1
        opcode = names.index(asm)
        opcode = int(opcode) * 100
        final = opcode
    
    return final

def assemble(program: str)-> (list,list):
    
    codes = []
    errors = []
    
    for line in program.split('\n')
        codes.append(encode(line))

    return codes , errors


def disassemble(start: int, end: int):
    """Displays assembly language listing of memory contents `start` to `end`"""
    for addr in range(start, end + 1):
        print(str(addr).rjust(2) + ": " + toAssembly(readMem(addr)))
    print()
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
# mattprog = [700, 399, 700, 398, 499, 613, 497, 198, 397, 499, 216, 399, 504, 497, 800, 0, 1]
# load(mattprog, [5,12])

if __name__ == "__main__":
    reset()
    