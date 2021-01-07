while True:
    pin_code = input("Enter pin code : ")
    if pin_code.isdigit() and len(pin_code) == 4 and len(pin_code) > 0:
        print("right pin!!!")
        break
    else:
        print("please enter right pin !!!")
        continue
print(pin_code)