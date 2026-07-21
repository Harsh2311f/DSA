#-----------For largest element in an array----------------
n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
print("Largest element =", largest)