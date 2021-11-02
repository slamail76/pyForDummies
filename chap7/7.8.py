# programma 7.8

frase = 'Quel ramo del lago di Como, che volge a mezzogiono'
lettera = input("Che lettera volete cercare ? ")
for carattere in range(len(frase)):
    if frase[carattere]==lettera:
        print(f'Ho trovato una {lettera} in posizione {carattere}')
else:
    print(f'Non ho trovato nessuna lettera {lettera} nella frase')
