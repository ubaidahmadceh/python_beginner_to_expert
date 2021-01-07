from collections import deque

my_list = ['pakistan', 'india', 'nepal']

deque_of_my_list = deque(my_list)
deque_of_my_list.popleft()

print(deque_of_my_list)