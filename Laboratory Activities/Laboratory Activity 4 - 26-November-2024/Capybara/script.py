from Capybara import Capybara

def test_capybara_cases():
    capybara1 = Capybara("Mochi", "F", 3)
    capybara2 = Capybara("Raijin", "M", 2)
    capybara3 = Capybara("Bond", "M", 5)
    capybara4 = Capybara("Pebbles", "F", 4)

    test_case_num = int(input("Enter the test case number: "))

    if test_case_num == 1:
        selected_capybara = capybara1
    elif test_case_num == 2:
        selected_capybara = capybara2
    elif test_case_num == 3:
        selected_capybara = capybara3
    elif test_case_num == 4:
        selected_capybara = capybara4
    else:
        print("Invalid test case number. Please choose 1-4 only.")
    

    print(f"Test Case {test_case_num}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")

test_capybara_cases()