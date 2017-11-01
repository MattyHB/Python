class Sudoku:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        string = ''
        num = 0
        while num < 9:
            string += str(self.board[num])
            string += '\n'
            num += 1
        return string

    def cell(self, x, y):
        xlevel = self.board[x]
        cell = xlevel[y]
        return cell

    def row(self, x):
        return self.board[x]

    def column(self, y):
        colLis = []
        for item in self.board:
            colLis.append(item[y])
        return colLis

    def complete(self):
        if 0 in self.board:
            return False
        else:
            return True
        
    def box(self, x, y):
        boxX = x // 3
        boxY = y // 3

        l = []
        for x in range(boxX*3, boxX*3 + 3):
            for y in range(boxY*3, boxY*3 + 3):
		l.append(s.cell(x,y))
	return l

    def possible(self, x, y):
        pos = [1,2,3,4,5,6,7,8,9]
        
        # check row
        for cell in self.row(x,y):
            if cell == 0:
		continue
            elif cell in pos:
		pos.remove(cell)
	# check column
        for cell in self.column(x,y):
            if cell == 0:
		continue
            elif cell in pos:
		pos.remove(cell)
	# check box
        for cell in self.box(x,y):
            if cell == 0:
		continue
            elif cell in pos:
		pos.remove(cell)
	return pos

    def solve(self):
        while not self.complete():
            if len(self.possible) == 1:
                # change the value to the only poss
                # if not, keep going
                #repeat till the second coming
                
            
            

puzzle = [  [0,9,0,1,0,0,0,0,6],
            [0,0,6,8,0,0,2,9,7],
            [5,7,0,0,0,0,1,0,8],
            [0,0,9,0,1,0,0,2,5],
            [7,0,0,9,0,4,0,0,3],
            [1,6,0,0,3,0,9,0,0],
            [6,0,3,0,0,0,0,4,9],
            [2,5,7,0,0,8,3,0,0],
            [9,0,0,0,0,6,0,8,0]]
