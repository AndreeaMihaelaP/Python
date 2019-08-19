#  Write a function that calculates how many vowels are in a string.

def countVowels(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count  = 0
    for i in sentence:
        for v in vowels:
            if i is v:
                count += 1
    return count            

def countVowels_1(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for s in sentence:
        if s in vowels:
            count += 1
    return count            
print(countVowels_1("Aeioddddddddda aa aa"))