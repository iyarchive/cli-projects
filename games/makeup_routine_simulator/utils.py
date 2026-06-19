import time
import sys

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def choose(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Choose 1-{len(options)}")
        except ValueError:
            print("Enter a number.")
