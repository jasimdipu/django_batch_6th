try:
    number = int(input())
    print(number/0)

except ValueError as e:
    print(e, "number value is not int")
except TypeError as e:
    print(e, "number is bigger then 100")
except ZeroDivisionError as e:
    print("from zero dev error section")
except Exception as e:
    print(e)
