"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.today()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor += item._valorItem
        self.valorNota=valor


    def imprimirNotaFiscal(self):
        print('-' * 112, "\nNOTA FISCAL {: > 92}/{}/{}".format(self._data.day, self._data.month, self._data.year))
        print("Cliente:  {}\tNome:  {} \nCNJP/CPF:{}".format(self._Id, self._cliente._nome, self._cliente._cnpjcpf))
        print("{}\nITENS\n{}".format('-' * 112,'-' * 112,))
        print("Seq  Descrição{:<10} QTD\tValor Unit{:<22}Preço\n{} {}    {}\t{} {:>29}".format('\t' * 6, ' ' ,'-' * 4, '-' * 51, '-' * 5, '-' * 10, '-' * 10))
        for a in self._itens:
            print("{:0>3}  {:<53}{:>5} \t {:>6.2f} {:>30.2f}".format(a.getSequencial(), a.getDescricao(), a.getQuantidade(), a.getValorUnitario(), a.getValorit()))
        print('_' * 112)
        