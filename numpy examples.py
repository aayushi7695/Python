from typing import Optional, Union, Tuple

from numpy import *
from numpy.core._multiarray_umath import ndarray

arr = array([1, 3.5, 4, 2, 5])
print(arr)
print(arr.dtype)

arr1 = linspace(0, 16, 10)
print(arr1)
print(arr1.dtype)

arr2 = linspace([0, 16, 15])
print(arr2)
print(arr2.dtype)
