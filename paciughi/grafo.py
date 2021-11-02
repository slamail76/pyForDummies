# Programma che genera un grafico a random
import random
import matplotlib.pyplot as plt

def casual():
    dado = random.randint(1,6)
    if (dado == 1) or (dado == 3) or (dado == 5):
        result = -1
        return(result)
    elif (dado == 2) or (dado == 4) or (dado == 6):
        result = 1
        return(result)

i = 50
assx = []
assy = []
delta = 0
p = 0
n = 0
for x in range(i):
    x += 1
    segno = casual()
    z = round(random.uniform(0.01,8),2)
    y = segno * z
    delta += y
    assx.append(x)
    assy.append(delta)
    print(x, "\t", y)

print(f'I valori positivi sono {p} mentre quelli negativi sono {n}')
plt.figure(figsize=(8,4), dpi=100)

plt.plot(assx,assy,'red')
plt.xlabel("Tentativi")
plt.ylabel("Valori")
plt.title('Curva di casualità del dado con segni + o -')
plt.grid()
plt.show()
