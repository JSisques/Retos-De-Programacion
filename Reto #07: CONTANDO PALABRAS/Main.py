'''
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
'''

def normalize(word):

    word = word.lower().replace(",", "").replace(".", "").replace("!", "")

    return word

def countWords(text):

    wordDict = {}

    words = text.split(" ")

    for word in words:
        normalizedWord = normalize(word)
        
        if wordDict.get(normalizedWord) != None:
            wordDict[normalizedWord] += 1
        else:
            wordDict[normalizedWord] = 1
    
    return wordDict
        

if __name__ == '__main__':
    print(countWords("Esto es una frase, esto es otra frase amigos."))