# Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui de-al 2-lea element din tuplă.
#  Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sortByThirdCharOfSecondElementOfTouple(*touples):
    return sorted(touples, key = lambda x: x[1][2])

print(sortByThirdCharOfSecondElementOfTouple(('abc', 'bcd'), ('abc', 'zza')))    