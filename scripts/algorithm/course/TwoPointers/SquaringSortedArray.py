def sorted_square(arr):
    left = 0
    right = len(arr) - 1
    output = [0 for x in arr]
    i = right

    while left < right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            output[i] = left_square
            left += 1
        else:
            output[i] = right_square
            right -= 1
        i -= 1
    return output
def main():
    arr1 = [-2, -1, 0, 2, 3]
    arr2 = [-3, -1, 0, 1, 2]
    c1 = sorted_square(arr1)
    c2 = sorted_square(arr2)
    print(c1)
    print(c2)


main()