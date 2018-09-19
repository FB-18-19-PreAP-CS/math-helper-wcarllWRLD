import math
#def main():
def compound_int(p,t,r):
    '''returns compound interest rounded to 2 decimals
            Principal, Years(or number of times compounded), Interest
            
        >>> compound_int(1000,1,1)
        1010.0
            
        >>> compound_int(2,100,10)
        27561.22
            
        >>> compound_int(5959,7,3.4)
        7530.38
            
        >>> compound_int(59.99,7,4.4)
        81.09
            
        >>> compound_int(71000.81,3,2.2)
        75790.71
            
        >>> compound_int(1000,-3,10)
        Traceback (most recent call last):
            ...
        ValueError: Time cannot be negitive.
        
    '''
    if t < 0:
        raise ValueError("Time cannot be negitive.")
    if r > 99:
            raise ValueError("Rate must be entered in percent and be below 100%.")
    r = r / 100
    r = r + 1
    out = float(p*r**t)
    out = round(out,2)
    return out
        

def sphere_volume(r):
    '''returns volume of sphere rounded to 3 decimals
        >>> sphere_volume(10)
        4188.79
        >>> sphere_volume(7.5)
        1767.146
        >>> sphere_volume(4.125)
        294.009
        >>> sphere_volume(-2)
        Traceback (most recent call last):
            ...
        ValueError: A sphere's radius cannot be negitive.
    '''
    if r < 0:
        raise ValueError("A sphere's radius cannot be negitive.")
    pi = math.pi
    return round((4/3)*pi*r**3,3)

def distance_formula(x1,y1,x2,y2):
    '''
        returns  the distance between two points in square root form.
        x1,y1,x2,y2 order of input
    >>> distance_formula(-3,1,0,-3)
    The distance is the Square root of 25.
    
    >>> distance_formula(-4,22,-10,-3)
    The distance is the Square root of 661.
    
    >>> distance_formula(-4,-4,-4,-4)
    The distance is the Square root of 0.
    '''
    part1 = round((x2-x1)**2 + (y2-y1)**2,3)
    
    return print(f"The distance is the Square root of {part1}.")
    
def midpoint(x1,y1,x2,y2):
    '''
    returns the midpoint of two points
    enter points in order of x1,y1,x2,y2
    
    >>> midpoint(2,3,6,6)
    (4.0, 4.5)
    '''
    
    return ((x1+x2)/2,(y1+y2)/2)










if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()
