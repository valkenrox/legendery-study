try:
    a = 10
    b = 0
    c = 5
    # x = a + b / c
    print(x)
except (NameError, ZeroDivisionError) as e:
    print("Variable a is not defined")
    print(e)
except Exception as e:
    print("Something went wrong")