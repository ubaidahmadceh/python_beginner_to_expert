class my_class:
    fruit = "Apple"

    @classmethod
    def show_fruit(cls):
        return f"Fruit name is : {cls.fruit}"  

print(my_class.show_fruit())  