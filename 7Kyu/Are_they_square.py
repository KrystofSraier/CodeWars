from math import sqrt

def is_square(n):
    if n == []:
        return None
    for i in n:
        if sqrt(i).is_integer() == True:
            pass
        elif sqrt(i).is_integer() == False:
            return False
    return True