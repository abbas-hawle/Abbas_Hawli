def calculate_finances():
    salary = float(input("Enter Nabiha's salary of the month: "))
    month = input("Enter the name of the month: ")
    savings_percentage = float(input("Enter the savings percentage: ")) / 100
    rent_percentage = float(input("Enter the rent percentage: ")) / 100
    electricity_percentage =float(input("Enter the electricity percentage: ")) / 100

    savings = salary* savings_percentage
    rent = salary* rent_percentage
    electricity = salary* electricity_percentage

    total_expenses =savings + rent + electricity
    remainder = salary - total_expenses
    yearly_rent = rent * 12
    yearly_electricity = electricity * 12
    additional_savings = 50
    savings_remainder = additional_savings / savings if savings != 0
    else 0

    print("\Financial Report")
    print(f"Month: {month}")
    print(f"Salary: ${salary:}")
    print(f"Savings: ${savings:}")
    print(f"Rent: ${rent:}")
    print(f"Electricity: ${electricity:")
    print(f"Total Expenses: ${total_expenses:}")
    print(f"Remainder: ${remainder:}")
    print(f"Yearly Rent: ${yearly_rent:}")
    print(f"Yearly Electricity: ${yearly_electricity:}")
    print(f"Salary Squared: ${salary_squared:}")
    print(f"Additional savings remainder: {savings_remainder:}")

    calculate_finances()