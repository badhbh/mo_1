import math

def gold_method_min(a, b, input_func, accuracy):
    output = {'minimum': None, 'calc_counter': 0}
    phi = (1 + math.sqrt(5)) / 2
    l = b - a
    x1 = b - l/phi
    x2 = a + l/phi
    while True:
        if(input_func(x1) >= input_func(x2)):
            a = x1
        else:
            b = x2
        if(abs(l) < accuracy):
            break
        c = (a + b) / 2
        output['minimum'] = [c]
        output['calc_counter'] += 1
    return output   

