def perfect_numbers(num):
    if not num.isdigit():
        return "Please enter a valid integer."

    num = int(num)
    sumv = 0

    for i in range(1,num):
        if num % i == 0:
            sumv += i

    if sumv == num:
        return f"{num} is a perfect number."
    else:
        return f"{num} is not a perfect number."
    
num = input("Enter a number: ")
print(perfect_numbers(num))   
