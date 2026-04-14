import argparse
from datetime import date
from tracker import init_db, add_expense, list_expenses, delete_expenses, monthly_summary, sort_by_category
from models import Category
def main():
    init_db()
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")
    subParser = parser.add_subparsers(dest="command")

    #add
    addParser = subParser.add_parser("add", help="Add a new expense")
    addParser.add_argument("amount", type=float, help="Amount of the expense")
    addParser.add_argument("notes", type= str, help="Notes for the expense")
    addParser.add_argument("--category", type=str,default="other",choices=["food", "transportation", "entertainment", "utilities", "other"], help="Category of the expense")


    #list
    listParser = subParser.add_parser("list", help="List expenses")
    listParser.add_argument("--month", type=int, help="Filter by month")
    listParser.add_argument("--year", type=int, help="Filter by year")

    #summary
    summaryParser = subParser.add_parser("summary", help="Monthly summary")
    summaryParser.add_argument("month", type=int, help="Month for summary")
    summaryParser.add_argument("year", type=int, help="Year for summary")

    #delete
    deleteParser = subParser.add_parser("delete", help="Delete an expense")
    deleteParser.add_argument("id", type=int, help="ID of the expense to delete")

    #categories
    categoriesParser = subParser.add_parser("categories", help="Show all available categories")

    #sorted
    sortedParser = subParser.add_parser("sorted", help="List expenses sorted by category")
    sortedParser.add_argument("--category", type=str, help="Filter by category", choices=["food", "transportation", "entertainment", "utilities", "other"])


    args = parser.parse_args()

    if args.command == "add":
        expense = add_expense(args.amount, args.notes, args.category)
        print(f"Added: [{expense.id}] {expense.amount} - {expense.notes} ({expense.category.value}) on {expense.date}`")
    elif args.command == "list":
        expenses = list_expenses(args.month, args.year)
        for expense in expenses:
            print(f"[{expense.id}] {expense.amount} - {expense.notes} ({expense.category.value}) on {expense.date}")
        total = sum(expense.amount for expense in expenses)
        print(f"Total: {total}")
    elif args.command == "summary":
        summary = monthly_summary(args.month, args.year)
        for category,total in summary.items():
            print(f"{category}: {total}")
    elif args.command == "delete":
        delete = delete_expenses(args.id)
        if delete:
            print(f"Deleted expense with ID {args.id}")
        else:            print(f"No expense found with ID {args.id}")
    elif args.command == "categories":
        print("Available categories:")
        for cat in Category:
            print(f"  • {cat.name}: {cat.value}")
    elif args.command == "sorted":
        expenses = list_expenses()
        sorted_expenses = sort_by_category(expenses)
        for category, category_expenses in sorted_expenses.items():
            print(f"{category}:")
            for expense in category_expenses:
                print(f"  • {expense.amount} - {expense.notes} on {expense.date}")

if __name__ == "__main__":
    main()
