'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def isPrime(num):

    prime = True
    count = 2

    while count < num and prime:
        if num % count == 0:
            prime = False 
        
        count += 1

    return prime

if __name__ == '__main__':
    
    for i in range(0, 101):
        print("Número ", str(i)," es primo? ", str(isPrime(i)))