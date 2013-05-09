def computeDeriv(poly) :
    #poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
    #power_limit = len(poly)
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
