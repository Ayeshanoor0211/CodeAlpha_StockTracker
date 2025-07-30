def stock_portfolio_tracker():
    
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2700,
        "AMZN": 3300,
        "MSFT": 290
    }

    portfolio = {}
    total_investment = 0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' to finish entering stocks.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Invalid stock symbol. Try again.")
            continue

        
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("Invalid quantity. Enter a number.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    print("\n--- Portfolio Summary ---")
    with open("portfolio_summary.txt", "w") as file:
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            total_investment += value
            line = f"{stock}: {qty} shares × ${price} = ${value}"
            print(line)
            file.write(line + "\n")

        total_line = f"Total Investment: ${total_investment}"
        print(total_line)
        file.write(total_line)

stock_portfolio_tracker()
