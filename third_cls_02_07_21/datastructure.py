# list, tuple, set, dictionary

# index = 0 -> n-1
l = [1, 2, 3, 4.5, 5.5, 5.5, 5.5, 6.5, "seven", "eight", "nine"]

print(l[1])
print(type(l[1]))
print(type(l))
print(l)
l.append("Ten")
print(l)

l.insert(2, 10)
print(l)

print(l.index("nine"))

print(l.count(5.5))

p = l.pop()
print(p)
print(l)

print(l.pop(0))
print(l)

l = [3, 5, 2, 6, 8, 19, 3, 8, 2, 5]
print("Befor sorting", l)
l.sort()
print('After sorting', l)
l.reverse()
print(l)

r = l.remove(19)
print(r)
print(l)

# nested list
l = [[1, 2, [3.1, 3.2, 3.3]], [4, 5, 6], [7, 8, 9]]

print(l[0][2][0])
# l2 = l[0][2]
# print(l2[0])

# immutable
l[0] = 100
print(l)
#
# for i in l:
#     print(type(i))
#     print(i)

print("#" * 50)

# tuple
# immutable
t = (1, 2, 3, 4, 5, 6)
print(t)
# t[0] = 100
print(t[3])
print(t.index(3))

print(t.count(2))

print("#" * 100)
# set
# immutable, no indexing
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 5, 5, 5}

print(type(s))
s.add(10)
print(s)
s2 = {6, 7, 8, 9}
print(s.union(s2))

print(s2.intersection(s))

print(s2.issubset(s))



