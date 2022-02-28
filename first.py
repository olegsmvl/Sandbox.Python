from collections import defaultdict
from email.policy import default


def common_elements (a, b):
    b_dict = defaultdict(int)
    for el in b:
            b_dict[el] += 1
    result = []

    for el in a:
        count = b_dict[el]
        if count > 0:
            result.append(el)
            b_dict[el] -= 1

    return result

if __name__ == "__main__":
    a = [1,2,3,2,0]
    b = [5,1,2,7,3,2]
    result = common_elements(a, b)
   # for el in result:
    print(result)