# Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian. 
# Sa se scrie o functie care primeste ca parametru o lista de puncte si returneaza o lista de tuple (a,b,c) unice 
# care reprezinta dreptele unice determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).

# formula ecuatia unei drepte (y-ya)/(x-xa) = (yb-ya)/(xb-xa)
def getDrepteFromPuncte(listOfPoints):
    ln = len(listOfPoints)
    listOfDrepte = []
    for i in range(0 , ln-1):
        for j in range( i+1 , ln ):
            a = listOfPoints[j][1] - listOfPoints[j][0]
            b = listOfPoints[i][0] - listOfPoints[i][1]
            c = listOfPoints[j][0] * listOfPoints[i][1] - listOfPoints[i][0] * listOfPoints[j][1]
            listOfDrepte.append((a,b,c))
    return listOfDrepte
    
print(getDrepteFromPuncte([(1,2),(-6,3),(4,-2)]))    