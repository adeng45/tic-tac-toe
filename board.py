import numpy as np
from constants import *

class Board:

    def __init__(self):
        self.arr = np.full( (ROWS, COLS) , '?')

    def mark(self, row, col, who):
        self.arr[row][col] = who

    def clear(self):
        self.arr = np.full( (ROWS, COLS) , '?')

    def show(self):

        for row in range(ROWS):
            
            print('[', end='')
            
            for col in range(COLS):
                print(self.arr[row][col], end='')
                if (col != COLS - 1):
                    print(', ', end='')

            print(']')

    def get(self, row, col):
        return self.arr[row][col]

    def fetch(self):

        for row in range(ROWS):
            for col in range(COLS):
                yield (row, col, self.get(row, col))



                
# Board().show()



