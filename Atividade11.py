from Atividade03 import Ponto
from Atividade03 import Quadrilátero
class Play:
    def P(self):
        x = int(input("qual a abscissa do ponto: "))
        y = int(input("qual a ordenada do ponto: "))
        s = Ponto(x,y)
        #definir ponto no plano
        print(s.qualQuadrante())
        x = int(input("qual a abscissa do quadrilatero: "))
        y = int(input("qual a ordenada do quadrilatero: "))
        c = Quadrilátero(x,y)
        #definir tamanho do quadrilátero
        print(c.contidoEmQ(s))

a = Play()
a.P()