def printDecimal(x):
    return f'{x: >7}'


def printOctal(x):
    d = oct(x)[2:]
    return f'{d: >6}'


def printHexadecimal(x):
    c = hex(x)[2:]
    return f'{c: >12}'


def printBinario(x):
    b = bin(x)[2:]
    return f'{b: >7}'


def imprimirTabela(n):
    print("Decimal\tOctal\tHexadecimal\tBinario\n"
          "-------\t------\t-----------\t-------\t")
    while n < 256:
        print(printDecimal(n), printOctal(n), printHexadecimal(n), printBinario(n))
        n += 1


a = 0
imprimirTabela(a)
