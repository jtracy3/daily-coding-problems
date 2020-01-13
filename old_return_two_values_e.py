# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def two_items_to_k(input, k):
    '''
    For any input list
    :param input: list of numerical values
    :param k: numerical value to check
    :return: boolean
    '''

    bool_list = list()

    for i in input:
        list_sum = [i + j for j in input if i != j]
        for val in list_sum:
            if val == k:
                bool_list.append(True)
            else:
                bool_list.append(False)

    return any(bool_list)

# check with a few examples
check = [[1,2,3,4,5], [3,6,8,9,10], [4,10,7,20,78]]
k = [9, 15, 50]
answer = [True, True, False]

for i in range(len(check)):
    l = check[i]
    k_ = k[i]
    x = two_items_to_k(l, k_)
    # vals = two_items_to_k(l, k_)[1]
    print(f'Do two items in our list add at the {k_}? {x}')

#########################################################
# try with random set of 100 dimensional integer vectors
import numpy as np

N = 10

for i in range(N):
    a = list(np.random.randint(low=0, high=1000, size=100))
    k = list(np.random.randint(low=0, high=1000, size=1))
    out = two_items_to_k(a, k)
    print(f'Random list of ints {a}\nRandom value to check \
          {k}\nDo any two values add to make k? {out}')
