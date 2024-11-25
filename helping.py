import  random

arr = []
for i in range(0,100):
    arr.append(random.randint(1,100))
print("Not sort", arr)
def counting_sort(array):
    max_znach = max(array)
    count = [0] * (max_znach + 1)
    for num in array:
        count[num] += 1
    sorted_array = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_array.append(i)
            count[i] -= 1

    return sorted_array
def count_sort(array, stepin):
    n = len(array)
    result = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (array[i] // stepin) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (array[i] // stepin) % 10
        result[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    for i in range(len(array)):
        array[i] = result[i]
def radix_sort(arr):
    max_num = max(arr)
    stepin = 1
    while max_num // stepin > 0:
        count_sort(arr, stepin)
        stepin *= 10
    return arr
sorted_arr = counting_sort(arr)
print("Sorted counting: ",sorted_arr)
sorted_arr = radix_sort(arr)
print("Sorted radix: ",sorted_arr)
