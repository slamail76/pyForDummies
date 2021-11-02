# programma 8.6

def tabellina(num):
    print(f'Tabellina del numero {num}')
    for n in range(1,11):
        print(f'{num} x {n} \t=\t{num*n}')

n = int(input("Inserisci un numero da 1 a 10 = "))
tabellina(n)
