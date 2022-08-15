'''
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def reverse(text):
    reversedText = ""

    for letter in text:
        reversedText = letter + reversedText

    return reversedText
        

if __name__ == '__main__':
    print(reverse("Hola mundo"))