Expense Tracker
A menu-driven Python command-line application for recording expenses and reviewing total and category-based spending. Built as a foundational project to practise Python functions, lists, dictionaries, loops and user input.
Features
- Add an expense with an item name, category and amount.
- View a numbered list of expenses.
- Edit an expense's item, category or amount.
- Delete an expense by its displayed number.
- Calculate total spending across all recorded expenses.
- Calculate spending for a specified category.
- Handle non-numeric expense selections and invalid expense numbers during editing and deletion.
Technology
- Python 3
- Built-in Python functionality only; no external packages are required.
- Expenses are stored in memory as a list of dictionaries.
Getting started
Download expense_tracker.py and open a terminal in the folder containing it. Run:
python3 expense_tracker.py
On systems where Python 3 is available as python, use python expense_tracker.py instead.
Usage
Choose a number from the menu:
Option	Action
1	Add expense
2	View expenses
3	Delete expense
4	Show total spending
5	Show category spending
6	Edit expense
7	Exit


For example, add these sample expenses using option 1:
Item	Category	Amount
Lunch	Food	150
Bus ticket	Transport	40
Coffee	Food	80


Option 4 displays total spending of ₹270.0. Choose option 5 and enter Food to see category spending of ₹230.0.

Category matching is case-sensitive: Food and food are treated as different categories. Total and category summaries display the rupee symbol; currency conversion is not supported.
Code organisation
The application is contained in expense_tracker.py:
Function	Purpose
main()	Initialise the expense list and run the menu loop
add_expense()	Collect and append an expense
view_expense()	Display the current expenses
delete_expense()	Remove an expense by its number
calculate_total()	Sum all expense amounts
category_total()	Sum amounts matching a category
edit_expense()	Update an expense field



Author
Kashvi Agrawal — B.Sc. Data Science and Scientific Computing student at Hochschule München.