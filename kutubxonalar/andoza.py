import re


def validate_phone_number(phone_number):
    """
    Validate a phone number in the format 998(7-9)XXXXXXXX.
    """
    regex = r"^998[7-9][0-9][0-9]{3}[0-9]{2}[0-9]{2}$"

    match = re.match(regex, phone_number)

    if match:
        print(f"The phone number '{phone_number}' is valid.")
        return True
    else:
        print(f"The phone number '{phone_number}' is invalid.")
        return False


phone_number_input = input("Please enter a phone number: ")
validate_phone_number(phone_number_input)
