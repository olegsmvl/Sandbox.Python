from enum import Enum


class Nums(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


s = set()
s.add(Nums.FIRST)
s.add(Nums.SECOND)
s.add(Nums.SECOND)

for item in s:
    print(item)

for item in s:
    print(item.value)

s.add(Nums.THIRD)
s_list = list(s)
print(s_list[2])
print(s_list[1])
print(s_list[0])

print("============")

set_union = set()
set_union.union(s)
print(s)
set_empty = set()
set_union.union(set_empty)
print(s)
set_empty = set()
