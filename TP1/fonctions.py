def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("que des entiers") 
    else :
    	return a ** b
