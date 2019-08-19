# Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def UpperToLower(str):
    str = str.replace(str[0], str[0].lower()) 
    for s in str[1:]:
        if s.isupper():
            print(s)
            str =  str.replace(s, '_' + s.lower())
    return str        

print(UpperToLower('UpperCamelCase'))