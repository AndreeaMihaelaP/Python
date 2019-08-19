# Find The largest common divisor of multiple numbers. Define a function with variable number of parameters to resolve this.
 
def cmmdc(*multipleNumbers):
    result  = multipleNumbers[0]
    for x in multipleNumbers[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result            

print(cmmdc(2,4,16))    