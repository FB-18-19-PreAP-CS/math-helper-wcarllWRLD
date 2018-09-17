import math

def compound_int(p,t,r):
    '''returns compound interest rounded to 2 decimals
        Principal, Years(or times compounded), Interest
        >>> compound_int(1000,1,1)
        1010
        
    
    '''
    r = r / 100
    r = r + 1
    out = float(p*r**t)
    out = round(out,2)
    return out


















