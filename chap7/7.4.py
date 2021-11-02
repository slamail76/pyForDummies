#programma 7.4
#indovina il numero con ciclo sempre vero ovvero while true

import random
numero = random.randint(1, 10)
numeroUtente = 0
tentativi = 1
print("Ho pensato un numero tra 1 e 10.\nHai a disposizione 3 tentativi per indovinarlo")
while True:
    numeroUtente = input("Indovina il numero premi invio per smettere ")
    if str(numeroUtente) == "":
        print("Ciao")
        break

    tentativi += 1
    numeroUtente = int(numeroUtente)
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
