#----------Reverse array--------------
arr = [10,20,30,40]
n = 0
i = len(arr) - 1
while n < i:
    arr[n], arr[i] = arr[i], arr[n]
    n += 1
    i -= 1
print(arr)