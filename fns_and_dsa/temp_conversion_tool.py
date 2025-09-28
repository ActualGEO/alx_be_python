CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSUIS_FACTOR = 5/9

def convert_to_celsuis(fahrenheit):
    """convert Fahrenheit to Celsuis."""
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSUIS_FACTOR


def convert_to_fahrenheit(celsuis):
    """convert to fahrenheit."""
    return (celsuis * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp = input("Enter the temperature to convert: ")
    question = input("Is this temperaturein celsuis or fahrenheit? (C/F): ")
    if question == "C":
        converted = convert_to_fahrenheit(float(temp))
        print(f"{temp}°C is {converted}°F")
    elif question == "F":
        converted = convert_to_celsuis(float(temp))
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsuis or 'F' for fahrenheit")

if __name__ == "_main_":
    main()