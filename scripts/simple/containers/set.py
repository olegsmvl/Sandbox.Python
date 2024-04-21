set_test = set()
set_test.add(1)
set_test.add(1)
set_test.add(2)
set_test.add(3)

print(set_test)

set_test.discard(5)
set_test.discard(2)
print(set_test)

set_test.clear()
print(set_test)
