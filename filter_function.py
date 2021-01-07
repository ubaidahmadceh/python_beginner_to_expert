number_list = [1, 2, 3, 4, 5]

def return_even(x):
    return x % 2 == 0

list_with_filter_function = list(filter(return_even, number_list))

print(number_list)

print(list_with_filter_function)