'''
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
'''

letterToMorseDict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " "
}

morseToLetterDict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z"
}

def convertToLetter(text):

    result = ""

    sentenece = text.split(" ")

    for letter in sentenece:
        result += str(morseToLetterDict.get(letter))

    result = result.replace("NoneNone", " ")

    return result

def convertToMorse(text):

    result = ""

    for letter in text:
        result += letterToMorseDict.get(letter.upper()) + " "


    return result

def convert(text):

    text = text.upper()

    if text.__contains__("A") or text.__contains__("E") or text.__contains__("I") or text.__contains__("O") or text.__contains__("U"):
        return convertToMorse(text)
    else:
        return convertToLetter(text)


        

if __name__ == '__main__':
    text = "Hola mundo a todos y todas"
    print("Texto a convertir: " + text + ". Texto convertido: " + str(convert(text)))

    text = ".... --- .-.. .-   -- ..- -. -.. ---   .-   - --- -.. --- ...   -.--   - --- -.. .- ..."
    print("Texto a convertir: " + text + ". Texto convertido: " + str(convert(text)))

    