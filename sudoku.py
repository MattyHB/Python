class Sudoku:
    def __init__(self, board):
        self.board = board
        self.complete = False

    def __repr__(self):
        string = ''
        num = 0
        while num < 9:
            string += str(self.board[num])
            string += '\n'
            num += 1
        return string

    def cell(self, x, y) -> int:
        xlevel = self.board[x]
        cell = xlevel[y]
        return cell

    def row(self, x, y):
        return self.board[x]

    def column(self, x, y):
        colLis = []
        for item in self.board:
            colLis.append(item[y])
        return colLis

    def iscomplete(self):
        if 0 in self.board:
            self.complete = False
        else:
            self.complete = True
        
    def box(self, x, y):
        boxX = x // 3
        boxY = y // 3

        l = []
        for x in range(boxX*3, boxX*3 + 3):
            for y in range(boxY*3, boxY*3 + 3):
                b = self.cell(x,y)
                l.append(b)
        return l

    def possible(self, x, y):
        pos = [1,2,3,4,5,6,7,8,9]
    # check row
        for cell in self.row(x,y):
            if cell == 0:
                continue
            elif cell in pos:
                pos.remove(cell)
    #Debugging
            print("Row Checked")
	# check column
        for cell in self.column(x,y):
            if cell == 0:
                continue
            elif cell in pos:
                pos.remove(cell)
    #Debugging
            print("Column Checked")

	# check box
        for cell in self.box(x,y):
            if cell == 0:
                continue
            elif cell in pos:
                pos.remove(cell)
            #Debugging
            print("Box Checked")
        self.iscomplete()
        return pos
    
    def step(self):
        # Not sure if this is right...
        for row in range(0,9):
            for column in range(0,9):
                temp = self.possible(row,column)
                if len(temp) == 1:
                    self.board[column][row] = temp
                    print("****** Item Added ******") 
        return self.board

    def solve(self):
        while self.complete == False:
            for row in range(0,9):
                for column in range(0,9):
                    temp = self.possible(row,column)
                    if len(temp) == 1:
                        self.board[column][row] = temp
                        print("****** Item Added ******") 
        return self.board
                
puzzle = [  [0,9,0,1,0,0,0,0,6],
            [0,0,6,8,0,0,2,9,7],
            [5,7,0,0,0,0,1,0,8],
            [0,0,9,0,1,0,0,2,5],
            [7,0,0,9,0,4,0,0,3],
            [1,6,0,0,3,0,9,0,0],
            [6,0,3,0,0,0,0,4,9],
            [2,5,7,0,0,8,3,0,0],
            [9,0,0,0,0,6,0,8,0]]

puzzle2 = [ [6,0,0,1,0,8,2,0,3],
            [0,2,0,0,4,0,0,9,0],
            [8,0,3,0,0,5,4,0,0],
            [5,0,4,6,0,7,0,0,9],
            [0,3,0,0,0,0,0,5,0],
            [7,0,0,8,0,3,1,0,2],
            [0,0,1,7,0,0,9,0,6],
            [0,8,0,0,3,0,0,2,0],
            [3,0,2,9,0,4,0,0,5]]

#For Debugger

p = Sudoku(puzzle)

p.solve()

print(p)