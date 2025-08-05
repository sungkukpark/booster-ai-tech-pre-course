def convert_celsius_to_fahrenheit(c):
    return (c * 1.8) + 32


def convert_fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


def main():
    print("This program converts Celsius → Fahrenheit and Fahrenheit → Celsius.")

    while True:
        try:
            mode = int(
                input(
                    "Please select a conversion mode first:\n1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius\n"
                )
            )
            if mode in [1, 2]:
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

    print("Mode has been selected.")

    # Example:
    # Celsius temperature: 32.2
    # Fahrenheit temperature: 89.96
    while True:
        try:
            temp = float(input("Please enter the temperature you want to convert: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    result = 0
    if mode == 1:
        result = convert_celsius_to_fahrenheit(temp)
    elif mode == 2:
        result = convert_fahrenheit_to_celsius(temp)
    else:
        raise NotImplementedError(f"{mode} is an undefined implementation.")

    print(f"The converted temperature is {result:.2f}.")


if __name__ == "__main__":
    main()
