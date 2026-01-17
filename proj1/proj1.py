#https://www.geeksforgeeks.org/python-program-to-find-largest-element-in-an-array/?ref=lbp
def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10, 13, 8, 1]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)