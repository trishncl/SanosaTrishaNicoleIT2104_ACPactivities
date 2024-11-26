def ExceptionHandling():
    try:
        size = int(input("Enter the size of the array: "))

        if size <= 0:
            print("The size must be positive integer.")
            return
        
        arr = [0.0] * size

        print("Enter the elements of the array: ")
        arr = [int(input()) for i in range(size)]


        idx = int(input("Enter the index of the element to print: "))
        print(f"Element at index {idx}:{arr[idx]: .2f}")

    except IndexError:
        print(f"Index {idx} is invalid.")

ExceptionHandling()