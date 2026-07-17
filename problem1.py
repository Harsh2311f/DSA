def OddEven(arr):
    odd = 0
    even = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd, even
arr = input("Enter the array elements: ").split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
odd, even = OddEven(arr)
print("Number of Odd elements:", odd)
print("Number of Even elements:", even)