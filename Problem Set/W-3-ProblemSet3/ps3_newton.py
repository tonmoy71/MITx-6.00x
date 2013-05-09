# 6.00x Problem Set 3 # # Successive Approximation: Newton's Method #


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...computeDeriv(
    power = 0
    result = 0

    for e in poly :
        result = result + e * x**power
        power += 1
    return result

# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].

    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    power = 0
    deriv = []

    for e in poly :
        if len(poly) == 1 :
            deriv.append(0.0)
            return deriv
        if power != 0 :
            deriv.append(float(power * e))
        power += 1
    return deriv

# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.

    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...

    def applyPower(poly, x) :
        """
        Calculates the value of the first derivative by multiplying the power of x (x is known value)
        with the list values
        """
        
        power = 0
        deriv_result = 0
        for e in poly :
            deriv_result += e * x**power
            power += 1
        return deriv_result  # value of the first derivative
            
        
    
##    poly = [1, 9, 8] 
##    x_0 = -3
##    epsilon = 0.0001
    x = x_0
    eval_Poly_Sum = 1
    iteration = 0
    result = []

    while abs(eval_Poly_Sum) > epsilon :
        eval_Poly_Sum = evaluatePoly(poly, x)  # gives value of f (x) 

        deriv_Poly_List = computeDeriv(poly)        # Calculates f ' (x),  gives a list of the co-efficients

        deriv_Poly_Sum = applyPower(deriv_Poly_List, x)  # value of f ' (x)
        
        x = x - (eval_Poly_Sum/deriv_Poly_Sum)

        iteration += 1
    result.append(x)
    result.append(iteration - 1)  # iteration is decreased by 1 because it is incremented before
                                           # the loop condition is satisfied
    return result
    
