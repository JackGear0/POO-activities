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
