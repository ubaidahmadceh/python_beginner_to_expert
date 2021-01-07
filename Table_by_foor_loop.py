integer = int(input("Enter integer to print table : "))
limit = int(input("Enter limit : "))
start = int(input("Enter start point : "))

for i in range(start, limit + 1): 
    print(f"{integer} x",i,"=",(integer * i))



