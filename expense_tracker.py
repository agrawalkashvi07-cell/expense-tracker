print("WELCOME TO YOUR EXPENSE TRACKER")

def main():
     expenses=[]

     while True:
          
          print("""
======== EXPENSE TRACKER ========

1. Add expense
2. View expenses
3. Delete expense
4. Show total spending
5. Show category spending
6. Edit expense
7. Exit
""")
          choice1=input("Enter your choice: ")
          if choice1=="1":
               add_expense(expenses)
          elif choice1 == "2":
               view_expense(expenses)
          elif choice1=="3":
               delete_expense(expenses)
          elif choice1=="4":
               total=calculate_total(expenses)
               print(f"Total spending: ₹{total}")
          elif choice1=="5":
               category = input("Enter the category: ")
               total = category_total(expenses, category)
               print(f"Total spent on {category}: ₹{total}")
          elif choice1=="6":
               edit_expense(expenses)
          elif choice1 == "7":
               print("Thank you for using Expense Tracker!")
               break
          

               

               
               

        

       


def add_expense(expenses):
    item=input("Enter the item whose expense you want to add : ")
    category=input("Enter the category to which the item belongs : ")
    amount=float(input("Enter the amount spent : "))
    exp={"item":item,"category":category,"amount":amount}
    expenses.append(exp)


def view_expense(expenses):
    if not expenses:
        print("No expenses found")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. Item:{expense['item']} | Category:{expense['category']} | Amount:{expense['amount']}")



def delete_expense(expenses):
    view_expense(expenses)

    while True:
        try:
            remove = int(input("Enter the number which expense would you like to delete: "))

            if 1 <= remove <= len(expenses):
                expenses.pop(remove - 1)
                print("Expense deleted successfully!")
                break
            else:
                print("Enter a valid expense number.")

        except ValueError:
            print("Please enter a number.")

def calculate_total(expenses):
    total=0
    for i in expenses:
        amt=i['amount']
        total+=amt
    return total

def category_total(expenses,category):
    total=0
    for i in expenses:
        if i['category']==category:
            amt=i['amount']
            total+=amt
    return total


def edit_expense(expenses):
    view_expense(expenses)
    choice= input('''What do you want to edit?
1. Item
2. Category
3. Amount''')
    
    if choice =="1":
        while True:
                try:
                    edit_item = int(input("Enter the number which expense would you like to edit: "))
                    if 1 <= edit_item <= len(expenses):

                        new_item=input("Enter the new item")

                        expenses[edit_item - 1]["item"] = new_item

                        print("Expense edited successfully!")
                        break
                    else:
                        print("Enter a valid expense number.")
        
                except ValueError:
                    print("Please enter a number.")

    elif choice =="2":
            while True:
                    try:
                        edit_category = int(input("Enter the number which expense would you like to edit: "))
                        if 1 <= edit_category <= len(expenses):
                            
                            new_category=input("Enter the new category")
    
                            expenses[edit_category - 1]["category"] = new_category
    
                            print("Expense edited successfully!")
                            break
                        else:
                            print("Enter a valid expense number.")
            
                    except ValueError:
                        print("Please enter a number.")
    elif choice =="3":
                while True:
                        try:
                            edit_amount = int(input("Enter the number which expense would you like to edit: "))
                            if 1 <= edit_amount <= len(expenses):
                                
                                new_amount=float(input("Enter the new amount"))
        
                                expenses[edit_amount - 1]["amount"] = new_amount
        
                                print("Expense edited successfully!")
                                break
                            else:
                                print("Enter a valid expense number.")
                
                        except ValueError:
                            print("Please enter a number.")
    
main()
            
        


    

    
    




        
