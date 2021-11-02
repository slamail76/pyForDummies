# programma 7.3
# Indovina il numero con limite di tentativi a 5
import random
numero = random.randint(1, 10)
numeroUtente = 0
tentativi = 1
print("Ho pensato un numero tra 1 e 10.\nHai a disposizione 3 tentativi per indovinarlo")
while numeroUtente != numero:
    numeroUtente = int(input("Prova a indovinarlo, inserisci un numero da 1 a 10 = "))
    tentativi += 1
    if numeroUtente == numero:
        print(f'Bravo ha indovinato il numero, era proprio il {numero}')
        break
    if tentativi > 3:
        print("Mi dispiace, non hai indovinato, tentativi finiti")
        print(numero)
        break
    elif numeroUtente > numero:
        print("Troppo grande, mi spiace non hai indovinato, ritenta")
    elif numeroUtente < numero:
        print("Troppo piccolo, mi spiace non hai indovinato, ritenta")
