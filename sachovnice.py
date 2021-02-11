# size = int(input("Zadej délku hrany šachovnice: "))
# symbols = ("#", ".")
# symbol_index = False
#
# for row in range(size):
#
#     for column in range(size):
#         print(symbols[symbol_index], end="")
#         symbol_index = not symbol_index
#
#     print()
#     symbol_index = not symbol_index

size = int(input("Zadej délku hrany šachovnice: "))
symbols = ("#", " ")
desk = list()

for row in range(size):
    desk_row = list()

    for column in range(size):
        symbol_index = (row + column) % len(symbols)
        desk_row.append(symbols[symbol_index])

    desk.append(desk_row)

for i in range(size):
    print("".join(desk[i]))
