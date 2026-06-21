sales = []

def record_sales(sales):

    while True:

        while True:

            product = input("Enter new product name: ").strip().lower().title()

            if product == "":
                print("Product name cannot be empty.")

            else:
                break
        
        while True:

            try:
                price = float(input("Enter price per product unit: ₱").strip())
                break
            
            except ValueError:
                print("That is not a number. Try again.")

        while True:

            try:
                units_sold = int(input("Enter amount of units sold: ").strip())
                break
            
            except ValueError:
                print("That is not a number. Please try again.")

        sales.append((product, price, units_sold))

        while True:

            user_choice = input("Do you want to record another transaction? Type 'yes' or 'no': ").strip().lower()

            if user_choice == "yes" or user_choice == "no":
                break

            else:
                print("Type 'yes' or 'no'.")


        if user_choice == "no":
                break


def analyze_sales(sales):

    revenues = [price * units_sold for product, price, units_sold in sales]

    total_revenue = sum(revenues)

    print(f"Your total revenue is ₱{total_revenue:.2f}.")

    top_sellers = [product for product, price, units_sold in sales if units_sold > 50]

    print("Your top sellers are:")

    if len(top_sellers) > 0:
        for product in top_sellers:
            print(f"    - {product}")
    
    else:
        print("There are no top sellers.")

    underperformers = [product for product, price, units_sold in sales if units_sold <= 10]

    print("Products that couldn't sell more than 10 units are:")

    if len(underperformers) > 0:
        for product in underperformers:
            print(f"    - {product}")
    
    else:
        print("There are no underperformers")

    avg_revenue = total_revenue/len(sales)

    print(f"Average revenue per product is ₱{avg_revenue:.2f}.")

def main(sales):

    record_sales(sales)

    analyze_sales(sales)

if __name__ == "__main__":
    main(sales)
