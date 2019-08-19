#  Write a function that returns the largest prime number from a string given as a parameter 
#  or -1 if the character string contains no prime number. 
#  Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271


def isPrime(number):
    number = int(number)
    if number > 1: 
        for i in range(2, int(number / 2)):
            if number % i == 0:
                return 0
        return 1
    return 0   
    


def largestPrime(s):
    listOfNumbers = []
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
    for i in newstr.split():
        if isPrime(i):
            listOfNumbers.append(int(i))
    return max(listOfNumbers)       

print(largestPrime('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))
