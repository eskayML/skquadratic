from math import sqrt





def formula(a,b,c):
    sol = '''
        _______
x = -b±√b²-4ac
    ____________
         2a

           __________
x = -({1})±√({1})²-4({0})({2})
       ________________
            2({0})

       _______
x = {5}±√ {3}
    ____________
         {4}

        
x = {5} ± {6}
    ___________
         {4}

x = {5} + {6}     OR     {5} - {6}
   _____________       __________  
       {4}                    {4}

x = {7}      OR   x = {8}


💥💥💥💥💥💥💥💥💥💥💥💥💥💥

'''
    D = b**2-4*a*c  
    if D < 0:
        return
    D = round(D,2)
    e = 2*a # 4
    f = -1 * b #5
    g = round(sqrt(D),2) #6
    
    y = round((f+g)/2,2) #7
    z = round((f-g)/2,2) #8
    
    
    return sol.format(a,b,c,D,e,f,g,y,z)


if __name__ == '__main__':
    print(formula(1,-5,6))