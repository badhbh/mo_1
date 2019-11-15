from input_function import input_func
from dichotomy_method import dichotomy_method
from gold import gold_method_min

print(dichotomy_method(-100, 100, input_func, 0.0001))

print(gold_method_min(-100, 100, input_func, 0.0001))
