def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("que des entiers")
    if a == 0 and b < 0:
        raise Exception("0 puissance négative est indéfini")
    resultat = 1
    for i in range(abs(b)):
        resultat = resultat * a
    if b < 0:
        return 1 / resultat
    return resultat
