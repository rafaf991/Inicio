def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    if x1-x2 == 0:
        raise Exception('la recta tiene pendiente infinita ')
        
    return float((y2-y1))/float((x2-x1))
	

def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0
    """
    return float(slope(x1,y1,x2,y2))*float((-x1)) + float(y1)
	


if __name__ == '__main__':
    import doctest
    doctest.testmod()


