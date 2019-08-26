# Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: (a intersectat cu b, a reunit cu b, a - b, b - a)

# def intersection(a,b):
#     result = [i for i in a if i in b] 
#     return result

# def union(a,b):
#     result = a + b
#     return result

def returnShitFromTwoLists(a, b):
    return ([set(a).intersection(b)], [set(a).union(b)], [set(a).difference(b)], [set(b).difference(a)])

# print(intersection([1,123,3,12,1],[1,123,22,1,12,3,2]))
# (union([1,123,4,43,12,1],[1,123,22,1,12,3,2]))
print(returnShitFromTwoLists([1,123,3,12,1],[1,123,22,1,12,3,2]))