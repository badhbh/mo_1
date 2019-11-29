import math


def gold_method_min(a, b, input_func, eps=1e-6):
    output = {'minimum': None, 'calc_counter': 0}
    phi = (1 + math.sqrt(5)) / 2

    while True:
        l = b - a
        x1 = b - l/phi
        x2 = a + l/phi
        if(input_func(x1) >= input_func(x2)):
            a = x1
        else:
            b = x2
        if(abs(l) < eps):
            break
        #c = (a + b) / 2
        output['minimum'] = [a, b]
        output['calc_counter'] += 1
    return output
