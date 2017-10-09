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
    """TODO: Removes and returns first number from inbox. If inbox is empty, returns 0."""
    return 0

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

# ---------------- Simulator "display" ----------------------

def dump():
    """TODO: Displays the state of memory/CPU"""
   #WAAAATTT?
    i = 0
    while i < 100:
        print(i + memory[i])
        i += 1
    print("Please implement me!")

def toAssembly(instr: int) -> str:
    """TODO: Returns assembly language translation of machine language instruction `instr`"""
    (command, locNum) = (instr // 100, instr % 100)
    locNum = str(locNum)
    
    assemblyPossible = [HLT, ADD, SUB, STA, LDA, BRA, BRZ, INP, OUT]
    
    '''if command == 1:
        command = "ADD "
    if command == 2:
        command = 'SUB '
    if command == 3:
        command = 'STA '
    if command == 5:
        command = 'LDA '
    if command == 6:
        command = 'BRA '
    if command == 7:
        command = "BRZ "
    final = (str(command) + str(locNum))
    if command == 9 and locNum == '1':
        final = 'INP'
    if command == 9 and locNum == '2':
        final = 'OUT'
    if command == 0:
        final = 'HLT'
    if locNum[0] == '0':
        locNum = locNum[:1]'''
    return final

def test_toAssembly():
    assert toAssembly(189) == "ADD 89"
    assert toAssembly(232) == "SUB 32"
    assert toAssembly(323) == "STA 23"
    assert toAssembly(501) == "LDA 1"
    assert toAssembly(622) == "BRA 22"
    assert toAssembly(743) == 'BRZ 43'
    assert toAssembly(901) == 'INP'
    assert toAssembly(902) == 'OUT'
    assert toAssembly(000) == 'HLT'


def disassemble(start: int, end: int):
    """Displays assembly language listing of memory contents `start` to `end`"""
    for addr in range(start, end + 1):
        print(str(addr).rjust(2) + ": " + toAssembly(readMem(addr)))

# ----------- Define shortcut names for interacti ve use

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


if __name__ == "__main__":
    reset()