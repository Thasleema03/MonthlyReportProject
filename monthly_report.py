# monthly_report.py
print("=== Monthly Report Generator ===")

month = input("Enter month name: ")

income = float(input("Enter total income: "))
expenses = float(input("Enter total expenses: "))
balance = income - expenses

print(f"\n--- {month} Summary ---")
print(f"Total Income: {income}")
print(f"Total Expenses: {expenses}")
print(f"Net Balance: {balance}")
