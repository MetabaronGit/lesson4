inpt = input("Hello, please write your numbers and press enter to confirm: ")
nums = ""
result = []

for char in inpt:
    if char.isnumeric():
        nums += char
    elif char == ",":
        result.append(int(nums))
        nums = ""

if nums != "":
    result.append(int(nums))

print(result)

# inpt = input('Hello, please write your numbers and press enter to confirm: ')
# nums = inpt.split(',')
# print(nums)
#
# result = []
# for num in nums:
#     num = int(num.strip())
#     result.append(num)
# print('List:', result)