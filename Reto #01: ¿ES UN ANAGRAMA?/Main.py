'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 '''

def isAnagram(word1, word2):

    res = True
    hashmap1 = {}
    hashmap2 = {}

    #Comprobamos que ambos Strings tengan la misma longitud
    if word1.__len__() != word2.__len__():
        res = False
    else:
        for i in range(0, word1.__len__()):
            letterWord1 = word1[i]
            letterWord2 = word2[i]

            if hashmap1.get(letterWord1) is not None:
                hashmap1[letterWord1] = hashmap1.get(letterWord1) + 1
            else:
                hashmap1[letterWord1] = 1

            if hashmap2.get(letterWord2) is not None:
                hashmap2[letterWord2] = hashmap2.get(letterWord2) + 1
            else:
                hashmap2[letterWord2] = 1
            
        for i in range(0, word1.__len__()):
            countLetter1 = hashmap1.get(word1[i])
            countLetter2 = hashmap2.get(word1[i])

            #print("Count letter 1: ", str(countLetter1))
            #print("Count letter 2: ", str(countLetter2))

            if countLetter1 != countLetter2 and res:
                res = False

    return res

if __name__ == '__main__':
    print(isAnagram("alrova", "alvaro"))
