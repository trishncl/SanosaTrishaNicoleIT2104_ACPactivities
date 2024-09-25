while True:
    amount = int(input("Enter the total purchase amount: "))
    amount_f = float(amount)
    print(f"Initial Purchase Amount: {amount_f:.2f}")

    if amount > 5000:
        discount = amount_f * 0.10
    else:
        discount = amount_f * 0.05

    print(f"Discount: {discount:.2f}")

    final_price = amount_f - discount
    print(f"Final Price: {final_price:.2f}")

    choice = input("Do you want to try again? (yes/no): ")
    if choice != "yes":
        print("Thank you!")
        break
