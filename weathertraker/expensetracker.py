import json
import os
import datetime 
FILE_NAME="expenses.json"
class Expense:
    """Expense model"""
    def __init__(self,title,category,amount):
        self.title=title
        self.category=category
        self.amount=amount
        self.date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    def to_dict(self):
        return {
            "title":self.title,
            "categroy":self.category,
            "amount":self.amount,
            "date":self.date
        }

def load_expenses():
    """load json data """
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open (FILE_NAME,"r")as file:
            data=json.load(file)

    except json.JSONDecodeError:
        print("corrupted error")
        return []
    except Exception as e:
        print("error",e)
        return []
    else :
        return data
    finally:
        print("load operation finished") 

def save_expenses(expenses:list):
    """save data"""
    try:
        with open (FILE_NAME,"w")as file:
            json.dump(expenses,file,indent=4)
    except Exception as e:
        print("save error",e)

def add_expense():
    """Add expenses"""
    try:
        title = input("title").strip()
        category = input("categroy").strip()
        amount = float(input("Amount"))
        if amount <=0:
            raise ValueError("positive amount only ")
        expense = Expense(title,category,amount) 
        expenses = load_expenses()
        expenses.append(expense.to_dict())

        save_expenses(expenses)
        print("expenses added")

    except ValueError as e:
        print(e)   

def list_expenses():
    expenses=load_expenses()

    if not expenses:
        print("not data")
        return 
    for i,exp in enumerate(expenses):
        print(f"{i}.{exp['title']} |"
              f"{exp['category']} | "
              f"rs{exp['amount']} "
              f"{exp['date']} "
              )
        
def filter_expenses():
    categroy=input("categroy")
    expenses=load_expenses()
    filtered=list(filter(lambda x:x['categroy'].lower()==categroy.lower(),
                         expenses))  

    if not filtered:
        print("no result")
        return 
    for exp in filtered:
        print(exp)

def summarize_expenses():
    expenses = load_expenses()

    amounts = list(map(lambda x:x["amount"],
                     expenses))
    total  =  sum(amounts)
    print("Total",total) 

def expenses_generator():
    expenses = load_expenses()

    for exp in expenses:
        yield exp

def show_title_categories():
    expenses = load_expenses()

    titles = [e["title"] for e in expenses]
    categoreies = [e["categroy"] for e in expenses]    


    for title,categoreies in zip(titles,categoreies):
        print(title,"-",categoreies)

def total_custom(*nums):
    print("custom total",sum(nums))

def show_user(**data):
    for key,value in data.items():
        print(key,value)

def validation_demo():
    expenses=load_expenses()

    amounts=[e["amount"] for e in expenses]
    print(any (a>1000 for a in amounts))
    print(all(a>0 for a in amounts))



def main():

    while True:

        print("\nExpense Tracker")
        print("1 Add")
        print("2 List")
        print("3 Filter")
        print("4 Summary")
        print("5 Generator Demo")
        print("6 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            summarize_expenses()

        elif choice == "5":
            for exp in expense_generator():
                print(exp)

        elif choice == "6":
            break

        else:
            print("Invalid")


if __name__ == "__main__":

    total_custom(10, 20, 30)

    show_user(
        name="Naval",
        role="Developer"
    )

    main()