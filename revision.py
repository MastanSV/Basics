#argumentsOrder
def argUnderstandCheck(a, b, c=20, *args, **kwargs):
    print(f'{a} {b} {c} {args} {kwargs}')

argUnderstandCheck(10, 20, 30, 40, 50, 60, 70, f=70, g=80, h=90, k=100)
#*in function args
def argsCheck(*, a, b, c, d):
    print(f'a {a}, b {b}, c {c}, d {d}')


argsCheck(10, 20, 30, 40, 50)
#argsCheck(a=10, 20, 30, 40, 50) # positional argumments can not be followed keyword arguments
argsCheck(a=10, b=20, c=30, d=40, e=50)
