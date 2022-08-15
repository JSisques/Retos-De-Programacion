'''
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 '''

def recursive(num):
    if num >= 101:
        return
    else:
        print(num)
        num += 1
        recursive(num)

def whileForm():
    count = 1

    while count < 101:
        print(count)
        count += 1

def forForm():
    for i in range(1, 101):
        print(i)

if __name__ == '__main__':
    recursive(1)
    whileForm()
    forForm()