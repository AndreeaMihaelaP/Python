#Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.

def isPrime(n):
    if n > 1:
        for i in range( 2 , int(n / 2)):
            if n % i == 0:
                return 0
        return 1        
    return 0

def primeList(*list):
    newList = []
    for i in list:
        if isPrime(i) == 1:
            newList.append(i)
    return newList  

print(primeList(1,2,3,4,5,7,7,9,11,14,13))