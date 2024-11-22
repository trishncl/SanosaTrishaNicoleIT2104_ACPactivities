def roman_to_integer(roman):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for char in roman:
        if char not in roman_values:
            return f"Please enter a valid Roman numeral."
    else:
        res = 0

        for i in range(len(roman)):
            if i + 1 < len(roman) and roman_values[roman[i]] < roman_values[roman[i + 1]]:
                res -= roman_values[roman[i]]
            else:
                res += roman_values[roman[i]]
        return f"The integer value of '{roman}' is: {res}"
    

roman = input("Enter a Roman numeral: ").strip().upper()
print(roman_to_integer(roman))


