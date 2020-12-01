"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto        import Produto
from cliente        import Cliente
from notafiscal     import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from tipocliente    import TipoCliente


def main():
    
    cli=Cliente(1, "Jose Maria", 100, "200.100.345-34", 1)
    
    p1=Produto(1,100,"Arroz Agulha", 5.5)
    it1=ItemNotaFiscal(1, 1, 10, p1)
    
    p2=Produto(2,200,"Feijão Mulatinho", 8.5) 
    it2=ItemNotaFiscal(2, 2, 10, p2)
    
    p3=Produto(3,300,"Macarrão Fortaleza", 4.5) 
    it3=ItemNotaFiscal(3, 3, 10, p3)


    nf = NotaFiscal(1,100,cli)
    
    nf.adicionarItem(it1)
    
    nf.adicionarItem(it2)
    
    nf.adicionarItem(it3)
    
    nf.calcularNotaFiscal()
    
    nf.imprimirNotaFiscal()
    print("{:0>3}  {}{:>47} \t {:>6.2f} {:>30.2f}".format(it1.getSequencial(), p1.getDescricao(), it1.getQuantidade(), p1.getValorUnitario(), it1.getValorit()))
    print("{:0>3}  {}{:>43} \t {:>6.2f} {:>30.2f}".format(it2.getSequencial(), p2.getDescricao(), it2.getQuantidade(), p2.getValorUnitario(), it2.getValorit()))
    print("{:0>3}  {}{:>41} \t {:>6.2f} {:>30.2f}".format(it3.getSequencial(), p3.getDescricao(), it3.getQuantidade(), p3.getValorUnitario(), it3.getValorit()))
    nf.resto()
    print("Valor Nota Fiscal= "+ str(nf.valorNota))


if __name__ == '__main__':
    main()


