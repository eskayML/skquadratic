from math import sqrt
import formula

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
            solution = formula.formula(self.a,self.b,self.c)
            if solution:
                print(solution)
            

equ = Quadratic(1,-5,6)
equ.solve()