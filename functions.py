'''
This file contains the correct functions to the student notebooks

'''

import numpy as np
from astropy.constants import G

#correct mass_bh function
def mass_bh_advanced(a, T):
    '''
    This function takes a (semi-major axis) in metres and T (period) in seconds (the data we are using already has everything in these units,
    so you don't have to change anything). This function also uses some constants like pi and G (gravitational constant) which are taken from
    python libraries.

    The function calculates M based on the formula we derived earlier and it returns the value calculated.
    Click the button below to reveal the solution to the function.
    '''
    #setting the constants
    G_value = G.value
    PI = np.pi
    
    #mass
    M = ((4*PI**2)/G_value)*((a**3)/(T**2))
    return M

#correct line function
def line(x,m,b):
    '''
    Curve_fit is a powerful tool because we can ask it to do many types of fits.

    For our purposes though, we want to define a fit of the line form.
    Define the line form below using x, m, and b (use * to multiply and + to add).
    '''
    y =   m*x + b

    return(y)
