# fruits(like = "apple", dis-like = "grapes")
from collections import namedtuple

name_tuple = namedtuple('fruits', 'Like, dislike')
values_in_tuple = name_tuple('Apple', 'Grapes')
print(values_in_tuple)


