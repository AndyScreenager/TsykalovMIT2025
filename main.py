def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Hello, World!')
n = int(input('n = '))
for i in range(n):
    print(f'{fib(i)}')
