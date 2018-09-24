import math
def main():
    print("Welcome to the math helper!")
    while True:
        print("")
        print("Type [quit] to quit.")

        select = input("[1] Compound Interest \n[2] Volume of a Sphere \n[3] Distance Formula \n[4] Midpoint \n[5] Area of a Semi-Circle \nPlease select your desired formula:")
        print('')
        print('')
        if select == "1":
            p = float(input('Enter your Principal:'))
            t = float(input('Enter the Amount of times your interest has been compounded:'))
            r = float(input('Enter your interest rate in % form:'))
            print(f'Your Principal of {p}, compounded {t} times, at a rate of {r}%, is now worth {compound_int(p,r,t)}!')
        elif select == "2":
            r = float(input('Input your sphere\'s radius:'))
            print(f'Your sphere with a radius of {r}, has a volume of {sphere_volume(r)}.')
        elif select == "3":
            x1 = float(input("Please input the X value for the first coordinate:"))
            y1 = float(input("Please input the Y value for the first coordinate:"))
            x2 = float(input("Please input the X value for the second coordinate:"))
            y2 = float(input("Please input the Y value for the second coordinate:"))
            print(f'Coordinates ({x1},{y1} and ({x2},{y2}), are the square root of {distance_formula(x1,y1,x2,y2)} apart.)')
        elif select == "4":
            x1 = float(input("Please input the X value for the first coordinate:"))
            y1 = float(input("Please input the Y value for the first coordinate:"))
            x2 = float(input("Please input the X value for the second coordinate:"))
            y2 = float(input("Please input the Y value for the second coordinate:"))
            print(f'The midpoint of coordinates ({x1},{y1}) and ({x2},{y2}) is {midpoint(x1,y1,x2,y2)}.')
        elif select == "5":
            r = float(input('Input your Semi-circle\'s Radius:'))
            print(f'Your Semi-circle with a Radius of {r} has an area of {area_semicircle(r)}.')
        elif select == 'quit' or select == 'Quit' or select == 'QUIT':
            print('Thank you for using The math helper!')
            break
        else:
            print("That is not a valid option!")
def compound_int(p,t,r):
    '''returns compound interest rounded to 2 decimals
            Principal, Years(or number of times compounded), Interest
            
        >>> compound_int(1000,1,1)
        1010.0
        
        >>> compound_int(0,0,0)
        0.0
        
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
        ValueError: Time cannot be negative.
        
    '''
    if t < 0:
        raise ValueError("Time cannot be negative.")
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
        >>> sphere_volume(0)
        0.0
        >>> sphere_volume(4.125)
        294.009
        >>> sphere_volume(-2)
        Traceback (most recent call last):
            ...
        ValueError: A sphere's radius cannot be negative.
    '''
    if r < 0:
        raise ValueError("A sphere's radius cannot be negative.")
    pi = math.pi
    return round((4/3)*pi*r**3,3)

def distance_formula(x1,y1,x2,y2):
    '''
        returns  the distance between two points in square root form.
        x1,y1,x2,y2 order of input
    >>> distance_formula(-3,1,0,-3)
    25
    
    >>> distance_formula(-4,22,-10,-3)
    661
    
    >>> distance_formula(-4,-4,-4,-4)
    0
    
    >>> distance_formula(-1,-2,-3,-4)
    8
    >>> distance_formula(-100,-200,-300,-400)
    80000
    '''
    #part1 = round((x2-x1)**2 + (y2-y1)**2,3)
    return round((x2-x1)**2 + (y2-y1)**2,3)
    #return print(f"The distance is the Square root of {part1}.")
    
def midpoint(x1,y1,x2,y2):
    '''
    returns the midpoint of two points
    enter points in order of x1,y1,x2,y2
    
    >>> midpoint(2,3,6,6)
    (4.0, 4.5)
    >>> midpoint(.25,-.25,-10,-20)
    (-4.875, -10.125)
    >>> midpoint(0,0,0,0)
    (0.0, 0.0)
    >>> midpoint(5,0,10,0)
    (7.5, 0.0)
    >>> midpoint(0,10,0,-20)
    (0.0, -5.0)
    '''
    
    return ((x1+x2)/2,(y1+y2)/2)



def area_semicircle(r):
    '''
    returns the area of a perfect semi circle.
    Input is radius. Rounds to 3 decimals.
    >>> area_semicircle(2)
    6.283
    >>> area_semicircle(0)
    0.0
    >>> area_semicircle(1000)
    1570796.327
    >>> area_semicircle(2.66)
    11.114
    >>> area_semicircle(-1)
    Traceback (most recent call last):
            ...
    ValueError: A Semi circle's radius cannot be negative!
    
    '''
    if r < 0:
        raise ValueError('A Semi circle\'s radius cannot be negative!')
    pi = math.pi
    return round((pi*r**2)/2,3)






if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
