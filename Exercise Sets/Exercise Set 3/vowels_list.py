instr = input("Enter a string: ")
list_instr = []

for x in instr:
    if x in "aeiouAEIOU":
        list_instr += [x, ]

print(list_instr)
