def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    max_product = arr[0] * arr[1]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
    return max_product

arr=[1,2,3,4,5]
print(max_product(arr))