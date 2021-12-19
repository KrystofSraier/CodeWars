/*
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

Notes
Array/list size is at least 2.

Array/list numbers could be a mixture of positives, negatives also zeroes .
*/

def adjacent_element_product(array):
    e = 0
    c = 1
    try:
        for i in array:
            b = array[c]
            d = i * b
            c += 1
            if i == array[0]:
                e = d 
            if d > e:
                e = d
    except:
        return e