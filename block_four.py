# Задача 1
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
max_index = arr.index(max(arr))
min_index = arr.index(min(arr))
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print("Массив после замены максимума и минимума:", arr)

# Задача 2
nums = []
print("Введите 10 целых чисел:")
for _ in range(10):
    nums.append(int(input()))
avg = sum(nums) / len(nums)
print("Среднее арифметическое:", avg)
for i in range(len(nums)):
    if nums[i] > avg:
        nums[i] = 1
print("Массив после замены:", nums)
