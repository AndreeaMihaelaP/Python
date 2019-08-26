# Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1,
# un numar variabil de siruri de caractere si un flag boolean setat default pe True. 
# Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele 
# care au codul ASCII divizibil cu x in caz ca flag-ul este setat pe True, 
# in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x. 
# Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]).
# Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere primite ca input.

def stringAndASCII( x = 1, flag = True, *strings):
    returnList = []
    for string in strings:
        auxList = []
        for letter in string:
            if flag == True:
                if ord(letter) % x == 0:
                    auxList.append(letter)
            else:
                if ord(letter) % x != 0:
                    auxList.append(letter)
        returnList.append(auxList)
    return tuple(returnList)

print(stringAndASCII(2, True, "test", "hello", "lab002"))


