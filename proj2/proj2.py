def sum(arr):
    count = len(arr)
    sum = arr[0]
    for i in range(1, count):
        sum += arr[i]
    return sum


arr = [1, 2, 3, 4, 5]
total = sum(arr)
print(total)

