#import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

#for line in sys.stdin:
    #print(line.split(), end="")
print("Type in your numbers")
print("ex: 4 2 3 | 4 2 3")
numbers = input()

list1, list2 = numbers.split("|")

# Remove leading/trailing spaces from each element in the lists
list1 = [int(x.strip()) for x in list1.split()]
list2 = [int(x.strip()) for x in list2.split()]

# Multiply corresponding elements and store in a new list
product_list = [list1[i] * list2[i] for i in range(len(list1))]

# Print the product list
print(*product_list)