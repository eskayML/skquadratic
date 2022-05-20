from math import sqrt
from formula import formula

class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.D = b**2-4*a*c
    
    def solve(method='formula'):
        '''
        parameters(method: default->formula)
        '''
        if method == 'formula':
            print(formula(self.a,self.b,self.c))
            



if __name__ == '__main__':
    equ = Quadratic(1,-4,4)
    equ.solve()