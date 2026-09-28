"""
 Expense Tracker 
-----------------------

"""
from array import array
from datetime import date

#------------------------------------------------------------------------------------------------
# OOP: A simple class representing a single expense
#------------------------------------------------------------------------------------------------
class Expense:
    def __init__(self,category:str, amount:float, note:str):
        self.category = category
        self.amount = amount
        self.note = note
        self.date = str(date.today())

    def __str__(self) -> str:
        return f"{self.date} | {self.category:<12} | Rs.{self.amount:>8.2f} | {self.note}"


#-------------------------------------------------------------------------------------------------
# OOP: A class that manages the whole collection of expenses
# ------------------------------------------------------------------------------------------------
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.amounts = array('d')

    def add_expense(self, category: str, amount: float, note:str) -> Expense:
        new_expense = Expense(category, amount, note)

        self.expenses.append(new_expense)
        self.amounts.append(amount)

        return new_expense
    def delete_expense(self, index:int) -> bool:

        if 0<= index < len(self.expenses):
            del self.expenses[index]
            del self.amounts[index]
            return True
        else:
            return False

    def get_total(self) -> float:

        total = 0.0

        for amt in self.amounts:
            total += amt

        return total

    def get_category_totals(self) -> dict:

        totals = {}

        for expense in self.expenses:

            if expense.category in totals:
                totals[expense.category] += expense.amount

            else:
                totals[expense.category] = expense.amount

        return totals

    def list_expenses(self) -> list:
        return self.expenses

    def count(self) -> int:
        return len(self.expenses)

#---------------------------------------------------------------------------------
# Functions: helper functions
#---------------------------------------------------------------------------------

def get_valid_amount() -> float:
        

        """ Keeps asking until a valid positive number is entered."""

        while True:
            text = input("Enter amount:")

            try:
                amount = float(text)

                if amount <=0:
                    print("Amount must be greater than zero. Try Again.")
                    continue
                return amount 

            except ValueError:
                print("That is not a valid number. Try Again.") 


def print_menu():
        

        print("\n==== EXPENSE TRACKER ====")
        print("1.Add expense")
        print("2.View all expenses")
        print("3.Delete an expense")
        print("4.Show total spending")
        print("5.Show category-wise totals")
        print("6.Exit")


def add_expense_flow(tracker:ExpenseTracker):
        category = input("Enter category:").strip()
        note = input("ENter note/description:").strip()

        amount = get_valid_amount()
        tracker.add_expense(category, amount, note) 
        print("Expense added successfully.")

def view_expenses_flow(tracker: ExpenseTracker):

        expenses = tracker.list_expenses()

        if tracker.count() == 0:
            print("No expenses recorded yet.")
            return
        print("\n---ALL EXPENSES---")

        for index, expense in enumerate(expenses):
            print(f"{index + 1}.{expense}")


def delete_expense_flow(tracker: ExpenseTracker):

        view_expenses_flow(tracker) 

        if tracker.count() == 0:
            return
        text = input("Enter the number of the expense to delete:")

        try:

            choice = int(text)
            index = choice - 1

            if tracker.delete_expense(index):
                print("Expense deleted.")
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid whole number.")

def show_total_flow(tracker:ExpenseTracker):
        total = tracker.get_total()

        print(f"Total amount spent: Rs. {total:.2f}")

def show_category_totals_flow(tracker:ExpenseTracker):
        totals = tracker.get_category_totals()

        if len(totals) == 0:
            print("No expenses to summarize yet.")
            return

        print("\n---Category-wise Totals---")
        for category, amount in totals.items():
            print(f"{category}:Rs.{amount:.2f}")


#------------------------------------------------------------------------
# Program entry point
# -----------------------------------------------------------------------
def main():
        tracker = ExpenseTracker()


        while True:

            print_menu()

            choice = input("Enter your choice(1-6):").strip()

            if choice == "1":
                add_expense_flow(tracker)

            elif choice == "2":
                view_expenses_flow(tracker)

            elif choice == "3":
                delete_expense_flow(tracker)

            elif choice == "4":
                show_total_flow(tracker)

            elif choice == "5":
                show_category_totals_flow(tracker)

            elif choice == "6":
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")


#---------------------------------------------------------------------------------------------
# Start the program
# --------------------------------------------------------------------------------------------

if __name__ == "__main__":
        
        main()
    
