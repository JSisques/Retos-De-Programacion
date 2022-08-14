'''
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
 '''

def bisiesto(year, numOfYears):

    if year % 4 != 0:
        if year % 2 == 0:
            year += 2
        else:
            if (year + 1) % 4 == 0:
                year += 1
            else:
                year += 3

    for i in range(0, numOfYears):
        print(year + 4 * i)


if __name__ == '__main__':
    bisiesto(2020, 30)