# coded on 10.11.2019


def dichotomy_method(a, b, input_func, accuracy):
    output = {'minimum': None, 'calc_counter': 0}
    c = (a+b)/2
    middle = input_func(c)

    while (b-a > accuracy):
        x = (a+c)/2
        y = (b+c)/2
        left = input_func(x)
        right = input_func(y)
        minimum = min(left, middle, right)

        if (minimum == left):
            b = c
            c = x
            middle = left
        elif (minimum == middle):
            a = x
            b = y
        else:
            a = c
            c = y
            middle = right

        output['minimum'] = [a, b]
        output['calc_counter'] += 2

    return output

