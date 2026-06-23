import sys

import my_functions

my_R = 5
my_gradient = 0.25
my_K = .8

Q = my_functions.compute_darcy(my_K, my_R, my_gradient)

print(Q)
