print(
    "This program converts the price of your makeup products into "
    "equivalent quantities of products you consume daily, helping "
    "you decide if they're worth buying."
)

while True:
    start = input("Are you ready to start? Input 'yes' or 'no': ").strip().lower()

    if start == "yes":
        break

    elif start == "no":
        quit()

    else:
        print("Please input a yes or no.")
        continue

while True:

    currency = input("Input your currency symbol (e.g. $, ₱, €): ").strip()
    
    if currency == "":
        print("Currency cannot be blank. Try again.")
        continue

    else:
        break

while True:

    products = {}

    while True:
        product_name = input("Input product name  (or 'stop' if no more items): ").strip().lower()

        if product_name == "stop":
            break

        try:
            product_price = int(input((f"Input price: {currency}")).strip())
            products[product_name] = product_price

        except ValueError:
            print("That is not a number. Try again.")

    while True:
        makeup_name = (input("Input makeup product name: ")).strip().lower()

        try:
            makeup_price = int(input((f"Input price: {currency}")).strip())
            break

        except ValueError:
            print("That is not a number. Try again.")

    print(f"{makeup_name.title()} ({currency}{makeup_price}) is equal to:")

    for product, price in products.items():
        print(f"        - {int(makeup_price / price)} {product.title()}s")

    while True: 

        another_session = input("Do you want to convert another product again? Input 'yes' or 'no'. ").strip().lower()

        if another_session == "yes":
            break

        elif another_session == "no":
            quit()

        else:
            print("Please input a yes or no.")
            continue
