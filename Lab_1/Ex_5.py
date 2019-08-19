# Write a function that checks whether a character string 
# contains special characters (\r, \t, \n, \a, \b, \f, \v)

def specialCharacters(str):
    specialChr =  ('\n', '\t', '\a', '\b', '\f', '\v')
    for c in str:
        if c in specialChr:    
            return True  
    return False
print(specialCharacters("line ada"))
