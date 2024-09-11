nine_tuple = ()

for x in range(9, 99, 9):
    nine_tuple += (x, )

print(f"Sliced Tuple: {nine_tuple[5:8]}")
