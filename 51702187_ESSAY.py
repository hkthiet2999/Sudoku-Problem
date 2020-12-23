import sys
import random
m=51702187
random.seed(m)

# 1 box trong 9x9 box
class box():
    def __init__(self):
        # num == so dc chon | exceptions == so bi loai
        self.num = " "
        self.exceptions = []
#  block 3x3
class latinSquare():

    def __init__(self):
        self.nums = []
        for x in range(3):
            row = []
            for y in range(3):
                row.append(box())
            self.nums.append(row)
        
        self.digits = ['0', '1', '2']
    # Check number truoc khi add vao box
    def available_numbers(self, row, col):
        available = []
        for num in self.digits:
            if self.is_legal(row, col, num) and num not in self.nums[row][col].exceptions:
                available.append(num)
        return available
    # Rules check number:
    def is_legal(self, row, col, num):
        return self.legal_in_box(row, col, num) and self.legal_in_col(col, num) and self.legal_in_row(row, num)

    def legal_in_box(self, row, col, num):
        row_start = int(row)
        col_start = int(col)
        for r in range(row_start, row_start):
            for c in range(col_start, col_start):
                if self.nums[r][c].num == num:
                    return False
        return True

    def legal_in_row(self, row, num):
        for c in range(3):
            if self.nums[row][c].num == num:
                return False
        return True

    def legal_in_col(self, col, num):
        for r in range(3):
            if self.nums[r][col].num == num:
                return False
        return True
    # build 1 box
    def build_box(self, row, col):
        digits = self.available_numbers(row, col)
        if len(digits) == 0:
            return False
        self.nums[row][col].num = digits[random.randint(0, len(digits)-1)]
        return True
    # build block 3x3 sudoku
    def build_latinSquare(self):
        row = col = 0
        while(row < 3):
            while(col < 3):
                if not self.build_box(row, col):
                    self.nums[row][col].exceptions = []
                    self.nums[row][col].num = " "
                    col -= 1
                    if col < 0:
                        col = 2
                        row -= 1
                    self.nums[row][col].exceptions.append(self.nums[row][col].num)
                else:
                    col += 1
            row += 1
            col = 0
    def print_latinSquare(self):
        ROW = [] # ROW[[COL[NUM]]]
        row = col = 0
        for row in range(3):
            if row == 0: 
                ROW = [ [ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)]]
                print(ROW[0])
            if row == 1: 
                ROW = [ [ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)]]
                print(ROW[0])
            if row == 2: 
                ROW = [ [ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)]]
                print(ROW[0])
            row += 1
#  1 Sudoku == 9 latinSquare == 9x9 box

class Sudoku():
    def __init__(self):
        self.nums = []
        for x in range(9):
            row = []
            for y in range(9):
                row.append(box())
            self.nums.append(row)
    # Print cmd
    def build_Sudoku(self):
        row = col = 0
        while(row < 9):
            if row == 0:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block1.nums[0][0].num
                    if col == 1:
                        self.nums[row][col].num = block1.nums[0][1].num
                    if col == 2:
                        self.nums[row][col].num = block1.nums[0][2].num
                    if col == 3:
                        self.nums[row][col].num = block2.nums[0][0].num
                    if col == 4:
                        self.nums[row][col].num = block2.nums[0][1].num
                    if col == 5:
                        self.nums[row][col].num = block2.nums[0][2].num
                    if col == 6:
                        self.nums[row][col].num = block3.nums[0][0].num
                    if col == 7:
                        self.nums[row][col].num = block3.nums[0][1].num
                    if col == 8:
                        self.nums[row][col].num = block3.nums[0][2].num
                    col += 1
            if row == 1:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block1.nums[row][0].num
                    if col == 1:
                        self.nums[row][col].num = block1.nums[row][1].num
                    if col == 2:
                        self.nums[row][col].num = block1.nums[row][2].num
                    if col == 3:
                        self.nums[row][col].num = block2.nums[row][0].num
                    if col == 4:
                        self.nums[row][col].num = block2.nums[row][1].num
                    if col == 5:
                        self.nums[row][col].num = block2.nums[row][2].num
                    if col == 6:
                        self.nums[row][col].num = block3.nums[row][0].num
                    if col == 7:
                        self.nums[row][col].num = block3.nums[row][1].num
                    if col == 8:
                        self.nums[row][col].num = block3.nums[row][2].num
                    col += 1
            if row == 2:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block1.nums[row][0].num
                    if col == 1:
                        self.nums[row][col].num = block1.nums[row][1].num
                    if col == 2:
                        self.nums[row][col].num = block1.nums[row][2].num
                    if col == 3:
                        self.nums[row][col].num = block2.nums[row][0].num
                    if col == 4:
                        self.nums[row][col].num = block2.nums[row][1].num
                    if col == 5:
                        self.nums[row][col].num = block2.nums[row][2].num
                    if col == 6:
                        self.nums[row][col].num = block3.nums[row][0].num
                    if col == 7:
                        self.nums[row][col].num = block3.nums[row][1].num
                    if col == 8:
                        self.nums[row][col].num = block3.nums[row][2].num
                    col += 1
            # block 456
            if row == 3:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block4.nums[0][0].num
                    if col == 1:
                        self.nums[row][col].num = block4.nums[0][1].num
                    if col == 2:
                        self.nums[row][col].num = block4.nums[0][2].num
                    if col == 3:
                        self.nums[row][col].num = block5.nums[0][0].num
                    if col == 4:
                        self.nums[row][col].num = block5.nums[0][1].num
                    if col == 5:
                        self.nums[row][col].num = block5.nums[0][2].num
                    if col == 6:
                        self.nums[row][col].num = block6.nums[0][0].num
                    if col == 7:
                        self.nums[row][col].num = block6.nums[0][1].num
                    if col == 8:
                        self.nums[row][col].num = block6.nums[0][2].num
                    col += 1
            if row == 4:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block4.nums[1][0].num
                    if col == 1:
                        self.nums[row][col].num = block4.nums[1][1].num
                    if col == 2:
                        self.nums[row][col].num = block4.nums[1][2].num
                    if col == 3:
                        self.nums[row][col].num = block5.nums[1][0].num
                    if col == 4:
                        self.nums[row][col].num = block5.nums[1][1].num
                    if col == 5:
                        self.nums[row][col].num = block5.nums[1][2].num
                    if col == 6:
                        self.nums[row][col].num = block6.nums[1][0].num
                    if col == 7:
                        self.nums[row][col].num = block6.nums[1][1].num
                    if col == 8:
                        self.nums[row][col].num = block6.nums[1][2].num
                    col += 1
            if row == 5:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block4.nums[2][0].num
                    if col == 1:
                        self.nums[row][col].num = block4.nums[2][1].num
                    if col == 2:
                        self.nums[row][col].num = block4.nums[2][2].num
                    if col == 3:
                        self.nums[row][col].num = block5.nums[2][0].num
                    if col == 4:
                        self.nums[row][col].num = block5.nums[2][1].num
                    if col == 5:
                        self.nums[row][col].num = block5.nums[2][2].num
                    if col == 6:
                        self.nums[row][col].num = block6.nums[2][0].num
                    if col == 7:
                        self.nums[row][col].num = block6.nums[2][1].num
                    if col == 8:
                        self.nums[row][col].num = block6.nums[2][2].num
                    col += 1
            # block 789
            if row == 6:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block7.nums[0][0].num
                    if col == 1:
                        self.nums[row][col].num = block7.nums[0][1].num
                    if col == 2:
                        self.nums[row][col].num = block7.nums[0][2].num
                    if col == 3:
                        self.nums[row][col].num = block8.nums[0][0].num
                    if col == 4:
                        self.nums[row][col].num = block8.nums[0][1].num
                    if col == 5:
                        self.nums[row][col].num = block8.nums[0][2].num
                    if col == 6:
                        self.nums[row][col].num = block9.nums[0][0].num
                    if col == 7:
                        self.nums[row][col].num = block9.nums[0][1].num
                    if col == 8:
                        self.nums[row][col].num = block9.nums[0][2].num
                    col += 1
            if row == 7:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block7.nums[1][0].num
                    if col == 1:
                        self.nums[row][col].num = block7.nums[1][1].num
                    if col == 2:
                        self.nums[row][col].num = block7.nums[1][2].num
                    if col == 3:
                        self.nums[row][col].num = block8.nums[1][0].num
                    if col == 4:
                        self.nums[row][col].num = block8.nums[1][1].num
                    if col == 5:
                        self.nums[row][col].num = block8.nums[1][2].num
                    if col == 6:
                        self.nums[row][col].num = block9.nums[1][0].num
                    if col == 7:
                        self.nums[row][col].num = block9.nums[1][1].num
                    if col == 8:
                        self.nums[row][col].num = block9.nums[1][2].num
                    col += 1
            if row == 8:
                while(col < 9):
                    if col == 0:
                        self.nums[row][col].num = block7.nums[2][0].num
                    if col == 1:
                        self.nums[row][col].num = block7.nums[2][1].num
                    if col == 2:
                        self.nums[row][col].num = block7.nums[2][2].num
                    if col == 3:
                        self.nums[row][col].num = block8.nums[2][0].num
                    if col == 4:
                        self.nums[row][col].num = block8.nums[2][1].num
                    if col == 5:
                        self.nums[row][col].num = block8.nums[2][2].num
                    if col == 6:
                        self.nums[row][col].num = block9.nums[2][0].num
                    if col == 7:
                        self.nums[row][col].num = block9.nums[2][1].num
                    if col == 8:
                        self.nums[row][col].num = block9.nums[2][2].num
                    col += 1
            # jump
            row += 1
            col = 0
    
    def print_Sudoku(self):
        ROW = [] # ROW[[COL[NUM]]]
        row = col = 0
        for row in range(9):
            if row == 0: 
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 1:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 2:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 3:
                print()
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 4:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 5:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 6:
                print()
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 7:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            if row == 8:
                ROW = [[ int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num)],[ int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num)],[int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]]
                print(ROW[0],ROW[1],ROW[2])
            row += 1

# ---------------------------------------------------------------------------------------
# Funcion in here
# # conversion
def getValue_ltSq(latin_Square):
    values = []
    for row in range(3):
        for col in range(3):
            value = latin_Square.nums[row][col].num
            values.append(value)
    return values
#  convers line by line
def conversion_to_Base(latinSquare,special_Num):
    result_Base = []
    for row in range(3):
        for col in range(3):
            result = int(latinSquare.nums[row][col].num) + 1 + int(special_Num)*3
            result_Base.append(result)
    return result_Base
    # return list chua values cua 1 latinSquare

# write File == print_Sudoku ( add values xong print thoi ko can` build tu` dau`)
def add_trueValues_intoSudoku(Sudoku):
    # Sudoku.nums[row][col].num = base_in_block'1-9'[0 den 8]
    row = col = 0
    while(row < 9):
        if row == 0:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block1[0]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block1[1]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block1[2]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block2[0]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block2[1]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block2[2]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block3[0]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block3[1]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block3[2]
                col += 1
        if row == 1:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block1[3]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block1[4]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block1[5]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block2[3]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block2[4]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block2[5]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block3[3]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block3[4]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block3[5]
                col += 1
        if row == 2:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block1[6]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block1[7]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block1[8]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block2[6]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block2[7]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block2[8]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block3[6]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block3[7]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block3[8]
                col += 1
        # block 456
        if row == 3:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block4[0]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block4[1]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block4[2]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block5[0]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block5[1]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block5[2]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block6[0]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block6[1]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block6[2]
                col += 1
        if row == 4:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block4[3]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block4[4]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block4[5]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block5[3]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block5[4]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block5[5]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block6[3]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block6[4]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block6[5]
                col += 1
        if row == 5:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block4[6]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block4[7]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block4[8]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block5[6]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block5[7]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block5[8]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block6[6]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block6[7]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block6[8]
                col += 1
        # block 789
        if row == 6:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block7[0]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block7[1]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block7[2]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block8[0]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block8[1]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block8[2]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block9[0]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block9[1]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block9[2]
                col += 1
        if row == 7:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block7[3]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block7[4]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block7[5]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block8[3]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block8[4]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block8[5]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block9[3]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block9[4]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block9[5]
                col += 1
        if row == 8:
            while(col < 9):
                if col == 0:
                    Sudoku.nums[row][col].num = base_in_block7[6]
                if col == 1:
                    Sudoku.nums[row][col].num = base_in_block7[7]
                if col == 2:
                    Sudoku.nums[row][col].num = base_in_block7[8]
                if col == 3:
                    Sudoku.nums[row][col].num = base_in_block8[6]
                if col == 4:
                    Sudoku.nums[row][col].num = base_in_block8[7]
                if col == 5:
                    Sudoku.nums[row][col].num = base_in_block8[8]
                if col == 6:
                    Sudoku.nums[row][col].num = base_in_block9[6]
                if col == 7:
                    Sudoku.nums[row][col].num = base_in_block9[7]
                if col == 8:
                    Sudoku.nums[row][col].num = base_in_block9[8]
                col += 1
        # jump
        row += 1
        col = 0
#  true sdk la sdk sinh ra sau khi conversion to base, chua swap row
def print_trueSudoku(Sudoku):
    for row in range(9):
        for col in range(9):
            print(Sudoku.nums[row][col].num, end=', ')
        print()
#  self === 1 sudoku da duoc add true values
# perfect_Sudoku return list chua true value, ko phai class Sudoku
def perfect_Sudoku(self):
    row = col = 0
    #  swap rows :
    row02 = row04 = row03 = row07 =  row06 =  row08 =  []
    #  giu nguyen
    row01 = row05 = row09 = []
    for row in range(9):
        if row == 0: 
            row01 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 1:
            row02 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 2:
            row03 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 3:
            row04 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 4:
            row05 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 5:
            row06 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 6:
            row07 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 7:
            row08 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        if row == 8:
            row09 = [int(self.nums[row][col].num),int(self.nums[row][col+1].num) , int(self.nums[row][col+2].num), int(self.nums[row][col+3].num), int(self.nums[row][col+4].num), int(self.nums[row][col+5].num),int(self.nums[row][col+6].num), int(self.nums[row][col+7].num), int(self.nums[row][col+8].num)]
        row += 1
    
    # swapLine(row02, row04)
    # swapLine(row03, row07)
    # swapLine(row06, row08)
    #complete sudoku:
    # print(row01) #
    # print(row04)
    # print(row07)
    # print(row02)
    # print(row05) #
    # print(row08)
    # print(row03)
    # print(row06)
    # print(row09) #
    pfSDK = [row01,row04,row07,row02,row05,row08,row03,row06,row09] # pfSDK = perfect sudoku
    return pfSDK

# digging hloes perfect sudoku sinh ra tu ham` perfect_Sudoku()
def dig_perfect_Sudoku(puzzle,holes):
    if holes == 9:
        # block 01:
        hole_in_block = 1 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 1
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 18:
        #
        # block 01:
        hole_in_block = 2 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 2
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 27:
        #
        # block 01:
        hole_in_block = 3 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 3
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 36:
        #
        # block 01:
        hole_in_block = 4 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 4
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 45:
        #
        # block 01:
        hole_in_block = 5 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 5
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 54:
        #
        # block 01:
        hole_in_block = 6 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 6
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 63:
        #
        # block 01:
        hole_in_block = 7 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 7
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    elif holes == 72:
        #
        # block 01:
        hole_in_block = 8 # hole_in_block = holes / 9
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1 
        # block 02:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 03:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(0,2)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 04:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 05:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 06:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(3,5)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 07:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(0,2)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 08:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(3,5)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
        # block 09:
        hole_in_block = 8
        while hole_in_block != 0 :
            r = random.randint(6,8)
            c = random.randint(6,8)
            if puzzle[r][c] != 0:
                puzzle[r][c] = 0
                hole_in_block -= 1
    else:
        #  do nothing
        pass
    # for i in range(9):
    #     for j in range(9):
    #         print(puzzle[i][j],end=',')
    #     print()
    return puzzle

def check_available_holes(holes):
    available = [9,18,27,36,45,54,63,72]
    for i in range(len(available)):
        if available[i] == holes:
            return True
    return False
# ---------------------------------------------------------------------------------------
#  MAIN IN HERE

# Generate 10 Latin Square
# 01
block1 = latinSquare()
block1.build_latinSquare()

# 02
block2 = latinSquare()
block2.build_latinSquare()

# 03
block3 = latinSquare()
block3.build_latinSquare()

# 04
block4 = latinSquare()
block4.build_latinSquare()

# 05
block5 = latinSquare()
block5.build_latinSquare()

# 06
block6 = latinSquare()
block6.build_latinSquare()

# 07
block7 = latinSquare()
block7.build_latinSquare()

# 08
block8 = latinSquare()
block8.build_latinSquare()

# 09
block9 = latinSquare()
block9.build_latinSquare()

# 10 - this is special Latin Square
special_latin_Square = latinSquare()
special_latin_Square.build_latinSquare()
# # ---------------------------------------------------------------------------------
# dig holes sdk
# holes = 9,18,27,36,45,54,63,72
holes = int(sys.argv[1])
output = sys.argv[2]
# CẦN PHẢI CHECK ARGUUMENT NỮA 
if check_available_holes(holes) == True:
    #-----------------------------------------------------------
    # #  # # Print cmd :
    sudoku = Sudoku()
    sudoku.build_Sudoku()
    sudoku.print_Sudoku() # 9 latin Square
    print()
    special_latin_Square.print_latinSquare() # Latin Square 10th
    #-----------------------------------------------------------
    # # # # Calculate
    # # Conversion to Base all 9 block
    arrValues = getValue_ltSq(special_latin_Square)
    # base_in_block = list [ vlues of 1 block ] len = 8
    base_in_block1 = conversion_to_Base(block1,arrValues[0])
    base_in_block2 = conversion_to_Base(block2,arrValues[1])
    base_in_block3 = conversion_to_Base(block3,arrValues[2])
    base_in_block4 = conversion_to_Base(block4,arrValues[3])
    base_in_block5 = conversion_to_Base(block5,arrValues[4])
    base_in_block6 = conversion_to_Base(block6,arrValues[5])
    base_in_block7 = conversion_to_Base(block7,arrValues[6])
    base_in_block8 = conversion_to_Base(block8,arrValues[7])
    base_in_block9 = conversion_to_Base(block9,arrValues[8])
    # # Generate perfect Sudoku 
    add_trueValues_intoSudoku(sudoku)
    # # Digging Sudoku
    puzzle_sdk = perfect_Sudoku(sudoku)
    puzzle_Sudoku = dig_perfect_Sudoku(puzzle_sdk,holes) # final result
    # -----------------------------------------------------------
    # # # # Write output file
    fOutput = open(output, 'w+')
    #fOutput.write(str(base_in_block9))
    for r in range(9):
        for c in range(9):
            fOutput.write(str(puzzle_Sudoku[r][c]))
            if c != 8:
                fOutput.write(', ')
        fOutput.write('\n')
    fOutput.close()
    # # # Add .txt
    # if os.path.exists(output+'.txt'):
    #     os.remove(output+'.txt')
    # # os.rename(output,output+'.txt')
else:
    print("Số lỗ không hợp lệ!")
# -----------------------------------------------------------
# Notes:
# // define :
# 1 sudoku = class Sudoku
# 1 class Sudoku = 9 class latinSquare = 9x9 class box
# 1 class latinSquare = 3x3 box | nickname = block
# // thuat toan :
# - Build 1 box -> Build latinSquare : 3x3 box == 1 latinSquare
# - Build Sudoku với values là 012 ( sd legal để check) từ các latinSqare  = 3x3LS = 9x9box
# - Get values trong lS10 ( block_Special ) để convers
# - Conversion to base từng value trong mỗi block
# - Add values đã convers vào sudoku đang có value 012 ( ghi đè )
# - Swap các row -> sinh ra đc 1 perfect sudoku
# - Đục lỗ : check holes == ok -> random dòng, cột trong mỗi block rồi đục lỗ, số lỗ -- cho đến khi == 0 thì ngừng.
# - Lấy argument, ghi file theo yêu cầu : import sys
#       + Build 10 latin square trc
#       + Check cac argument
#       + Chay thuat toan
# Author : Hoang Kien Thiet - 51702187 