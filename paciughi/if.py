#Esempio di operatore ternario
"""L'operatore ternario su può usare quando abbiamo da soddisfare
   un solo if ovvero un solo passaggio if else su una singola riga
   In tal caso è possibile inserire l'intera condizione all'interno
   di una variabile che restiuirà una stringa diversa a secondo della
   condizione vera """

numero = input("Inserisci un numero intero = ")
risposta = "è un numero pari" if int(numero)%2==0 else "è un numero dispari"
print(risposta)