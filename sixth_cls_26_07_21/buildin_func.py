# sum -> iteration function
# print(sum([1, 2, 4, 5, 6, 8, 9]))
l = [1, 2, 3, 45, 6, 7, 8, 90]


# iterator function -> range (build in)
# for i in range(10):
#     print(i)


# generator function/custom iterator
def myrange(val):
    for i in range(0, val):
        yield i


val = myrange(10)
print(next(val))
print(next(val))
print(next(val))
print(next(val))


def fahrenhite(T):
    return ((float(9) / 5) * T + 32)


def celcius(T):
    return (float(9) / 5) * (T - 32)


temp = [20, 30, 19, 48.40, 26]

print(list(map(fahrenhite, temp)))
print(list(map(celcius, temp)))

from functools import reduce


def getsum(a, b):
    return a + b


print(reduce(getsum, temp))

# lambda
getnumber = lambda a, b: a * b

print(getnumber(10, 10))

print(reduce(lambda a, b: a + b, temp))

getNumberIfGraterthen100 = lambda a: a if a > 100 else "a is smaller then 100"
print(getNumberIfGraterthen100(120))
