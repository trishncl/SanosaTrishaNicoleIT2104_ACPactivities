while True:
    amount = float(input("Enter the total purchase amount: "))
    print(f"Initial Purchase Amount: {amount:.2f}")

    if amount > 5000:
        discount = amount * 0.10
    else:
        discount = amount * 0.05

    print(f"Discount: {discount:.2f}")

    final_price = amount - discount
    print(f"Final Price: {final_price:.2f}")

    choice = input("Do you want to try again? (yes/no): ")
    if choice != "yes":
        print("Thank you!")
        break
