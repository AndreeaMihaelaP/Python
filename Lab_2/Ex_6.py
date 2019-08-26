# Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x. 
# Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
#  Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3, 4] 
# 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.

def listInList(n,*lists):
    hashmap = {}
    retList = []
    for list in lists:
        for element in list:
            if element in hashmap:
                aux = hashmap.get(element)
                aux = aux + 1
                hashmap[element] = aux
            else: 
                hashmap[element] = 1
    for key in hashmap.keys():
        print(hashmap)
        if hashmap[key] == n:
            retList.append(key)
    return retList        

print(listInList(2, [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"]))