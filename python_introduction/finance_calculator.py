user_income = int(input("Enter your monthly income:"))
user_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = user_income - user_expenses
projected_savings = int(monthly_savings * 12 +(monthly_savings *12 * 0.05))
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with intrest, is: {projected_savings}.")