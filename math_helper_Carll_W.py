from math import *

def compound_int(p,r,t):
    r = r / 100
    r = r + 1
    return float(p*r**t)

def circle_volume(r):
    return 4*3.14*r**3