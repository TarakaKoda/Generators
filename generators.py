def square_of_num(nums):
    square = []
    for num in nums:
        square.append(num *num)
    return square

numbers = [1,2,3,4,5]
result = square_of_num(numbers)
print(result)
# list comprehension
num = [x*x for x in numbers]
print(num)
# generators
square = (x*x for x in numbers)
for nums in square:
    print(nums)

def square_of_num(nums):
    for num in nums:
        yield (num * num)

output = square_of_num([1,2,3,4,5])
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
list1 = list(output)
print(list1)
for num in list1:
    print(num)