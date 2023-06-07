def add(*args):
    soma = 0
    for n in args:
        soma += n
    return soma


print(add(2, 4, 2, 6, 2))


# def calculate(n, **kwargs):
#     n += kwargs[""]