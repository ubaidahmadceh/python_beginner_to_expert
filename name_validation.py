while True:
    name = input("Enter Your Name : ")

    if name.isalpha() and (len(name) > 2 and len(name) <= 10):
        print("Right name")
        break
    else:
        print("please enter right name ")
        continue

print(name)