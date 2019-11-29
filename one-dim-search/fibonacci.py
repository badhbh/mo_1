# coded on 15.11.2019
import math


def fibonacci(n):
    return int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))


def fibonacci_method_min(a, b, input_func, eps=1e-6):
    output = {'minimum': None, 'calc_counter': 0}
    N = 0
    while ((b-a) / eps >= fibonacci(N)):
        N += 1
    N -= 1
    fib0 = fibonacci(N - 2)
    fib1 = fibonacci(N - 1)
    fib2 = fibonacci(N)
    x1 = a + (fib0/fib2) * (b - a)
    x2 = a + (fib1/fib2) * (b - a)
    while b - a > eps:
        x1 = a + (fib0/fib2) * (b - a)
        x2 = a + (fib1/fib2) * (b - a)
        if input_func(x1) < input_func(x2):
            b = x2
        elif input_func(x1) > input_func(x2):
            a = x1
        else:
            a = x1
            b = x2
        output['calc_counter'] += 2
    output['minimum'] = [a, b]
    return output
