# Console-Based Stock Portfolio Tracker

STOCK_OPTIONS = {
    "Apple": "AAPL",
    "Google": "GOOGL",
    "Tesla": "TSLA",
    "Airtel": "AIRTEL",
    "Jio": "JIO"
    
}

portfolio = {}

def display_menu():
    print("\n📊 Stock Portfolio Tracker")
    print("1. View Portfolio")
    print("2. Add or Update Stock")
    print("3. Remove Stock")
    print("4. Exit")

def display_portfolio():
    print("\n📊 Current Portfolio Status:\n")
    total_value = 0
    total_shares = 0

    for name, symbol in STOCK_OPTIONS.items():
        if symbol in portfolio:
            shares = portfolio[symbol]["shares"]
            price = portfolio[symbol]["price"]
            value = shares * price
            print(f"{name} ({symbol}): {shares} shares @ ${price:.2f} = ${value:.2f}")
            total_value += value
            total_shares += shares
        else:
            print(f"{name} ({symbol}): 0 shares")

    print("\n" + "-" * 40)
    print(f"📈 Total Shares Owned: {total_shares}")
    print(f"💰 Total Portfolio Value: ${total_value:.2f}\n")

def add_or_update_stock():
    print("\nAvailable stocks:")
    for i, name in enumerate(STOCK_OPTIONS.keys(), 1):
        print(f"{i}. {name}")
    choice = input("Enter stock name: ").strip()

    if choice not in STOCK_OPTIONS:
        print("❌ Invalid stock name.")
        return

    try:
        shares = int(input("Enter number of shares: "))
        price = float(input("Enter price per share: "))
        symbol = STOCK_OPTIONS[choice]
        portfolio[symbol] = {"shares": shares, "price": price}
        print("✅ Stock added/updated successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for shares and price.")

def remove_stock():
    choice = input("Enter stock name to remove: ").strip()

    if choice in STOCK_OPTIONS:
        symbol = STOCK_OPTIONS[choice]
        if symbol in portfolio:
            del portfolio[symbol]
            print("✅ Stock removed from portfolio.")
        else:
            print("⚠️ Stock not found in portfolio.")
    else:
        print("❌ Invalid stock name.")

# Main loop
while True:
    display_menu()
    option = input("Choose an option (1-4): ")

    if option == "1":
        display_portfolio()
    elif option == "2":
        add_or_update_stock()
    elif option == "3":
        remove_stock()
    elif option == "4":
        print("👋 Exiting the Portfolio Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid option. Please choose between 1 and 4.")
