import calculator  # Import calculation functions from calculator.py


def parse_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def main():
    # Connect each operator to its corresponding calculator function
    operations = {
        "+": calculator.add,
        "-": calculator.sub,
        "*": calculator.mul,
        "/": calculator.div,
    }

    print("Calculator (enter c to clear or q to quit)")

    while True:
        # Ask the user for the first number
        first_value = input("Enter a first number: ").strip()

        # Exit the program if the user enters q
        if first_value.lower() == "q":
            print("Thank you for using the calculator.")
            return

        # Convert the first input into a number
        try:
            result = parse_number(first_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        while True:
            # Ask the user which operation they want
            op = input(
                "Enter an operation (+, -, *, /), c to clear, or q to quit: "
            ).strip()

            # Exit the program if the user enters q
            if op.lower() == "q":
                print("Thank you for using the calculator.")
                return

            # Start a new calculation if the user enters c
            if op.lower() == "c":
                print("Cleared.")
                break

            # Check whether the entered operator is supported
            if op not in operations:
                print("Invalid operation. Please enter +, -, *, or /.")
                continue

            # Ask the user for the second number
            second_value = input("Enter the second number: ").strip()

            # Exit the program if the user enters q
            if second_value.lower() == "q":
                print("Thank you for using the calculator.")
                return

            # Convert the second input into a number
            try:
                operand = parse_number(second_value)
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Prevent division by zero
            if op == "/" and operand == 0:
                print("Error: Division by zero is not allowed.")
                continue

            # Perform the selected operation and store the new result
            previous_result = result
            result = operations[op](previous_result, operand)
            if (
                isinstance(previous_result, int)
                and isinstance(operand, int)
                and isinstance(result, float)
                and result.is_integer()
            ):
                result = int(result)

            # Display the current result
            print(f"Result: {result}")


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
