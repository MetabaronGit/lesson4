start = int(input("START: "))
stop = int(input("STOP: "))
divisor = int(input("DIVISOR: "))
final_list = []

print("Numbers in range({0}, {1}) divisible by {2}:".format(start, stop + 1, divisor))

if divisor == 0:
    print("Cannot divide by zero")
else:
    for i in range(start, stop + 1):
        if i % divisor ==0:
            final_list.append(i)
    print(final_list)

    # start = int(input('START: '))
    # stop = int(input('STOP: '))
    # divisor = int(input('DIVISOR: '))
    # result = []
    # if divisor:
    #     for num in range(start, stop + 1):
    #         if num % divisor == 0:
    #             result.append(num)
    #     print('Numbers in range(' + str(start) + ', ' + str(stop) + ') divisible by ' + str(divisor) + ':')
    #     print(result)
    # else:
    #     print('Cannot divide by zero')