'''
Fazer uma sequencia de impressão onde sejam mostras as representações
  decimal, octal, hexadecimal dos valores inteiros de 0 a 225 (que
  são os valores que um byte pode representar).
Verificar o contéudo dos especificadores de representação no
contexto do comando print. Cria para cada representação uma função
especifica (printDecimal, printOctal, printHexadecimal, printBinario).
Incluir no código uma funcionalidade imprimirTabela() que executar
 um laço para imprimir cada linhado relatório.
Layout da saída:
Decimal  Octal  Hexadecimal    Binario
------------- --------- --------------------- -----------------
  999      XXXX       XXXX          99999999
'''


def Dec(x):
    return f'{x: >7}'


def Oct(x):
    d = oct(x)[2:]
    return f'{d: >6}'


def Hex(x):
    c = hex(x)[2:]
    return f'{c: >12}'


def Bin(x):
    b = bin(x)[2:]
    return f'{b: >7}'


def Print_Table(n):
    print("Decimal\tOctal\tHexadecimal\tBinario\n"
          "-------\t------\t-----------\t-------\t")
    while n < 256:
        print(Dec(n), Oct(n), Hex(n), Bin(n))
        n += 1


a = 0
Print_Table(a)
