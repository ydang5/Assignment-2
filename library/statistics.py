# data_input = input("Please enter a series of data and use[]")
# Max and Min
def get_max(data_input)
    i = 0
    max = 0
    while i < len(data_input):
        datum = data_input[i]
        i = i + 1
        if datum > max:
            max = datum

def get_min(data_input)
    i = 0
    min = 100
    while i < len(data_input):
        datum = data_input[i]
        i = i + 1
        if datum < min:
            min = datum

# Mean

def get_mean(data_input)
    sum = 0

    for datum in data_input:

        sum = datum + sum

    len = len(data_input)

    mean = sum/len


# Median
def get_median(data_input)
# STEP 1: Organize the list of numbers from greater to lower.
    data_input.sort()
    # STEP 2: Find the "Middle value".
    # The following code will tell me if the number is odd or even. I took this info
    # from the following link: https://www.c-sharpcorner.com/blogs/python-program-to-check-odd-or-even1
    a = len(data_input)

    def find_middle(input_list):
       """
       Code taken from https://stackoverflow.com/a/38130999
       """
       middle = float(len(input_list))/2
       return (input_list[int(middle)], input_list[int(middle-1)])
    # STEP 2 (A): Find median with EVEN middle value.
    middle_value = 0
    if(a%2==0): #Even Odd Program using Modulus Operator (the)

       x, y = find_middle(data_input)
       middle_value = (x + y) / 2
    # STEP 2 (B): Find median with ODD middle value.
    els
       middle_index = float(len(data_input))/2

       middle_value = data_input[int(middle_index - .5)]


# mode, standard deviation, variance

import statistics
#1 Given array data, find single mode value

def get_mode(data_input)

    mode = statistics.mode(data_input)


#3 Given array data, find range


def get_standard_deviation(data_input)

# 4. Given array data, find standard deviation

# print standard deviation
# xbar is set to default value of 1
    value = statistics.stdev(data_input)

def get_variance(data_input)

# 5. Given array data, find variance
# creating a simple data - set

# Prints standard deviation
# xbar is set to default value of 1
    value = statistics.variance(data_input)
