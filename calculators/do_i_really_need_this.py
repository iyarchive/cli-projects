print("Are you hesitating if you should buy that item or not?"
      "\nWell, you should try our calculator to calculate how"
      " many hours or days of work you have to do to earn"
      " that item. Best of luck!")

while True:

    currency = input("Input your currency symbol (e.g. $, ₱, €): ").strip()
    
    if currency == "":
        print("Currency cannot be blank. Try again.")
        continue

    else:
        break

while True:

    try:
        monthly_salary = int(input(f"Input your monthly salary in numbers: {currency}").strip())
        break

    except ValueError:
        print("That is not a number. Try again.")

while True:

    try:
        num_of_workdays = int(input("How many days per week do you work: ").strip())
        break

    except ValueError:
        print("That is not a number. Try again.")

while True:

    try:
        daily_work_hours = int(input("How many hours per day do you work: ").strip())
        break

    except ValueError:
        print("That is not a number. Try again.")

weekly_salary = monthly_salary / 4.33
daily_salary = weekly_salary / num_of_workdays
hourly_salary = daily_salary / daily_work_hours

while True:

    try: 
        item_price = int(input(f"Input item price: {currency}").strip())
        break
        
    except ValueError:
        print("That is not a number. Try again.")

if item_price >= monthly_salary:
    item value = 
    print(f"This item is worth {item_price / monthly_salary:.2f} months of your time.")

elif item_price >= weekly_salary:
    print(f"This item is worth {item_price / weekly_salary:.2f} weeks of your time.")

elif item_price >= daily_salary:
    print(f"This item is worth {item_price / daily_salary:.2f} days of your time.")

else:
    print(f"This item is worth {item_price / hourly_salary:.2f} hours of your time.")
