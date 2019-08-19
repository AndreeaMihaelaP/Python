# Give a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and
#  a number (whole or float). Evaluate the polynomial for the given value.
#Horner method

def horner( poly, x):
    result = poly[0]
    for i in range(1 , len(poly)):
        result = result*x + poly[i]
    return result
# Let us evaluate value of 
# 3x3 + 5x2 - 2x - 5 for x = 3 
poly = [3 , 5 , -2 , -5 ] 
x = 3
  
print("Value of polynomial is " , horner(poly, x))     