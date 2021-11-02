# programma 8.6

def area_cerchio(raggio):
    import math
    return math.pi*raggio**2


raggio = int(input("Inserisci il valore del raggio : "))
print(f'L\'area del cerchio con raggio {raggio} è {area_cerchio(raggio)}')
