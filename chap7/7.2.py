#programma 7.2
#Indovina il numero
import random
numero = random.randint(1,10)
numeroUtente = 0
print("Ho pensato un numero tra 1 e 10")
while numeroUtente != numero:
    numeroUtente = int(input("Prova a indovinarlo, inserisci un numero da 1 a 10 = "))
    if numeroUtente == numero:
        print(f'Bravo ha indovinato il numero, era proprio il {numero}')
        break
    elif numeroUtente > numero:
        print("Troppo grande, mi spiace non hai indovinato, ritenta")
    elif numeroUtente < numero:
        print("Troppo piccolo, mi spiace non hai indovinato, ritenta")
