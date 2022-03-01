from collections import defaultdict
from unittest import result

def max_num_guests(guests: List[tuple]) -> int:
    res = 0
    arriving = defaultdict(int)
    leaving = defaultdict(int)

    for guest in guests:
        arriving[guest[0]] += 1
        leaving[guests[0]] += 1
    
    current = 0

    for day in sorted(set(arriving.keys().union(set(leaving.keys()))):
        current -= leaving[day]
        current += arriving[day]

        if current > res:
            res = current


if __name__ == "__main__":
    vec = [(1,2),(1,2)(1,2)(1,2)]
    result = max_num(vec)
    print(result)