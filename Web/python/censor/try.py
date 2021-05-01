try:
    i = int(input("enter any number: "))
    c = 1/i
    print(c)
except ValueError as e:
    print("exception 1 occured")
    print(e)
except ZeroDivisionError as e:
    print("make sure you are not dividing by zero")
    

print('code executed')