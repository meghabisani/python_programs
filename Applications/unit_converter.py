"""
Converts various units between one another.
"""


def len_converter():
    result = 0
    print("Length Converter: \n1) Foot to Inch \n2) Yard to Feet \n3) mm to cm "
          "\n4) cm to m \n5) m to km \n6) km to mile")
    choice = int(input("Enter your option: "))
    value = float(input("Enter the value you want to convert: "))

    if choice == 1:
        result = value * 12
    elif choice == 2:
        result = value * 3
    elif choice == 3:
        result = value / 10
    elif choice == 4:
        result = value / 100
    elif choice == 5:
        result = value / 1000
    elif choice == 6:
        result = value * 0.6214
    else:
        print("Incorrect Option")

    return result


def temp_converter():
    result = 0
    print("Temperature Converter: \n1) Degree Celsius to Kelvin \n2) Kelvin to Degree Celsius "
          "\n3) Degree Celsius to Fahrenheit "
          "\n4) Fahrenheit to Degree Celsius")

    choice = int(input("Enter your option: "))
    value = float(input("Enter the value you want to convert: "))

    if choice == 1:
        result = value + 273
    elif choice == 2:
        result = value - 273
    elif choice == 3:
        result = (value * 9/5) + 32
    elif choice == 4:
        result = 5/9 * (value - 32)
    else:
        print("Incorrect Option")

    return result

def converter():
    repeat = True
    print("Welcome to the UNIT CONVERTER!!\n")

    while repeat:
        try:
            print("\nFollowing Types of Converter are Available: \n1) Length \n2) Temperature ")
            user_input = int(input("Please enter the converter no you want to use(1 or 2): "))
        except:
            print("Please enter Integer only!!")
            continue
        else:
            if user_input == 1:
                result = len_converter()
            elif user_input == 2:
                result = temp_converter()
            else:
                print("Please Enter the correct option")
                continue

        print("Converted unit: ",result)
        choice = input("Do you want to convert again: (yes/no)")
        if choice[0].lower() == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    converter()