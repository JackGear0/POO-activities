class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def setx(self, x):
        self._x = x
        
    def setY(self, y):
        self._y = y    

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def qualQuadrante(self):
        if (self._x == 0 ) & (self._y ==0):
            return 'Origem'
        elif (self._x > 0 ) & (self._y > 0):
            return 1
        elif (self._x < 0 ) & (self._y > 0):
            return 2
        elif (self._x < 0 ) & (self._y < 0):
            return 3
        elif (self._x > 0 ) & (self._y < 0):
            return 4


class Quadrilátero:
    def __init__(self, P2, P1):
        self.P2 = P2 
        #P2 eixo X
        self.P1 = P1
        #P1 eixo Y
     
    def contidoEmQ(self, ponto):
        if (self.P1 >= ponto.getY() > 0 ) & (self.P2 >= ponto.getX() > 0):
            return True
            #1º quadrante
        elif (self.P1 >= ponto.getY() > 0 ) & (self.P2 >= ponto.getX() < 0):
            return True
            # 2º quadrante
        elif (self.P1 <= ponto.getY() < 0) & (self.P2 <= ponto.getX() < 0):
            return True
            #3º quadrante
        elif (self.P1 <= ponto.getY() < 0) & (self.P2 <= ponto.getX() > 0):
            return True
            # 4º quadrante
        else:
            return False
        
'''
if __name__ == '__main__':
    s = Ponto(-1,-1)
    #definir ponto no plano
    print(s.qualQuadrante())
    c = Quadrilátero(-5,-4)
    #definir tamanho do quadrilátero
    print(c.contidoEmQ(s))
'''
