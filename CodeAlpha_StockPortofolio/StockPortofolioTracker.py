
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 400
}

portfolio = {}
total_investment = 0

print("--- Stock Portfolio Tracker ---")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock ticker (or type 'done' to finish): ").strip().upper()
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not found in price database. Please try again.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity must be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid input! Please enter a valid integer for quantity.")

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    val = qty * price
    total_investment += val
    print(f"{stock}: {qty} shares @ ${price} = ${val}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save output to file
save_option = input("\nDo you want to save this summary to a file? (y/n): ").strip().lower()
if save_option == 'y':
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Saved to 'portfolio_summary.txt' successfully!")
