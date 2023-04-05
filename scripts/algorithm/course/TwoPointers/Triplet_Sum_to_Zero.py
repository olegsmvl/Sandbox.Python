def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        target = -arr[i]
        left = i+1
        search_pair(target,left,arr,triplets)

    return triplets

def search_pair(target, left,arr, triplets):
    right = len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if target == sum:
            triplets.append([-target, arr[left], arr[right]])
            right -= 1
            left += 1
        elif target < sum:
            right -= 1
        elif target > sum:
            left += 1

def main():
    a = [-3, 0, 1, 2, -1, 1, -2]
    print(search_triplets(a))
    b = [-5, 2, -1, -2, 3]
    print(search_triplets(b))
    c = [-3, 0, 1, 2, -1, 1, -2, -8, -12]
    print(search_triplets(c))


main()