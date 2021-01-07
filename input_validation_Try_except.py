list = []
def users_name():
    while True: # Never ending loop
        try:
            name = str(input("Please enter your first name: "))
            if (len(name) > 2 and name.isalpha()):
                list.append(name)
                break
            else:
                raise TypeError
        except TypeError:
            print("Letters only please.")
            continue # This causes it to continue
        except EOFError:
            print("Please input something....")
            continue # This causes it to continue

users_name()