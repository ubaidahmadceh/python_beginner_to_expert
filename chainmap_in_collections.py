from collections import ChainMap
dictionary_1 = {
    "like" : "Apple",
    "Dislike" : "Grapes" 
}
dictionary_2 = {
    "liked" : "Mango",
    "Disliked" : "Gauva" 
}
list_using_chainmap = ChainMap(dictionary_1, dictionary_2)
print(list_using_chainmap)

