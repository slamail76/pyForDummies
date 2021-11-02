# PROGRAMMA 7.5
# Conto alla rovescio
conteggio = int(input("Scegli un numero di partenza  "))
print(f'Conto alla rovescio da {conteggio} a 0')
for x in range(conteggio, -1, -1):  # conteggio è il valore di partenza, -1 quello di arrivo, -1 lo step
    print(x)
print("Ho finito")
