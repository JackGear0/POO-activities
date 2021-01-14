import random
def games():
    y=[]
    x=1
    while x < 61:
        y.append(x)
        x +=1
    lista =[]
    for x in range(6):
        tol=(random.choice(y))
        lista.append(tol)
        y.remove(tol)
    lista.sort()
    print(lista)
g=0
x = int(input("Quantos jogos deseja fazer? "))
while g != x:
    games()
    g +=1