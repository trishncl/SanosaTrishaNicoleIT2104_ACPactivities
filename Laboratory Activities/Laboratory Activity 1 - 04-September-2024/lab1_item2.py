char_one, char_two = input("Enter two space-separated characters: ").split()
larger_char = max(char_one, char_two)

print("-----------------------------------------------------")
print(f"The character with greater value is: {larger_char}")
print("-----------------------------------------------------")

print("Showing ASCII Values:")
asciiVal1 = ord(char_one)
print(f"{char_one} : {asciiVal1}")
asciiVal2 = ord(char_two)
print(f"{char_two} : {asciiVal2}")