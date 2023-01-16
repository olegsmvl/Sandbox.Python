def remove_duplicates(arr):
    i = 0
    next_non_duplicates = 1
    while(i < len(arr)):
        if arr[next_non_duplicates - 1] != arr[i]:
            arr[next_non_duplicates] = arr[i]
            next_non_duplicates += 1
        i += 1
    return  next_non_duplicates

def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()