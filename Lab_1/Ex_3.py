#Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. 
# Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )

def countWords(sentence):
    replacements = (',', '-', '!', '?', ';')
    for r in replacements:
        sentence = sentence.replace(r, ' ')
    return len(sentence.split())
    
print(countWords("Hey, you - what are you doing here!?"))

