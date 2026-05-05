import matplotlib.pyplot as plt

# -------- Test Case 1: Line Chart (Monthly Sales) --------
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 22000, 20000, 25000, 27000]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.show()


# -------- Test Case 2: Pie Chart (Expenses Distribution) --------
categories = ['Rent', 'Salaries', 'Utilities', 'Marketing', 'Others']
expenses = [30000, 50000, 10000, 15000, 8000]

plt.figure(figsize=(6, 6))
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Expense Distribution')
plt.show()

