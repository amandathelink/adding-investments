investments = []

def add_investment(amount):
    investments.append(amount)
    print("Investment of $", amount, "added successfully.")

def total_investments():
    total = sum(investments)
    print("Total investments: $", total)

while True:
    print("Choose an option:")
    print("1. Add investment")
    print("2. Display total investments")
    print("3. Quit")
    
    choice = input("Enter choice (1, 2 or 3): ")
    
    if choice == '1':
        amount = float(input("Enter amount invested: "))
        add_investment(amount)
    elif choice == '2':
        total_investments()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
