#0, 1, 1, 2, 3, 5, 8
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b #RHS evaluated first (1, 0+1) -> (1, 1) -> unpack this tuple and assign it to a, b
        print(a, b)


for num in fib(5):
    print(num)