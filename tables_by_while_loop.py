number = int(input("enter number : "))
start = int(input("enter start point : "))
limit = int(input("enter limit : "))


while start <= limit:
    print(f"{number} x {start} = {number*start}")
    start += 1

