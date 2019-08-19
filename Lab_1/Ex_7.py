# Write a function that receives a char_len integer and a variable number of strings (strings) and 
# check that each two neighboring strings follow the following rule: the second string starts with 
# the last char_len characters of the first string (like the word game pheasant).

def pheaseant(char_len, *strings):
        countTrue = 0
        countFalse = 0    
        for i in range(len(strings) - 1):
                print(strings[i][-char_len:], strings[i + 1][0:char_len])
                if strings[i][-char_len:] == strings[i + 1][0:char_len]:
                        countTrue += 1
                else:
                        countFalse += 1              
        if countTrue == len(strings) - 1:
                return True
        else:
                return False        


print(pheaseant(2, 'mare', 'repede', 'departe'))    
