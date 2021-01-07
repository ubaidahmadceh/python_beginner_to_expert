class my_class:
    def __init__(self):
        self.fruit = "Apple"

    def show_fruit(self):
        return f"Fruit name is : {self.fruit}"

my_object = my_class()
print(my_object.show_fruit())