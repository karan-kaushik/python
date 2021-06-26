
def total_operations(arr):
    # arr = [0] * 3
    # arr[0] = num0
    # arr[1] = num1
    # arr[2] = num2
    arr.sort()

    # count = arr[0]
    # arr[2] = arr[2] - arr[0]
    # arr[0] = 0
    # arr.sort()
    # count = count + arr[1]
    # arr[2] = arr[2] - arr[1]
    # arr[1] = 0
    # print(arr)
    # print(count)
    count = 0
    arr_length = len(arr) - 1
    for num in range(arr_length):
        count = count + arr[num]
        arr[arr_length] = arr[arr_length] - arr[num]
        arr[num] = 0
        arr.sort()
    # print(arr)
    print(count)


if __name__ == "__main__":
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        int_array = [int(x) for x in input().split()]
        total_operations(int_array)
