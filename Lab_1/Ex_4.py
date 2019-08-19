# Write a function that receives two strings as parameters 
# and returns the number of occurrences of the first string in the second.

def countAppearenceOfString(str1, str2):
    return str2.count(str1)

print(countAppearenceOfString('ana', 'ana nas ana ana aa'))