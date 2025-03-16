def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Hello, World!')
n = int(input('n = '))
print(f'fib({n}) = {fib(n)}')
