from input_function import input_func
from dichotomy_method import dichotomy_method
from gold import gold_method_min
from func_min import find_func_min
from fibonacci import fibonacci_method_min
import math

print(dichotomy_method(0, math.pi, input_func))
print(gold_method_min(0, math.pi, input_func))
print(fibonacci_method_min(0, math.pi, input_func))

#find_func_min(0, input_func, 0.1)