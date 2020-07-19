# Name:         Roger Silva Santos Aguiar
# Function:     This module creates a phone number with 10 digits.
# Initial date: July 19, 2020
# Last update:  July 19, 2020

class PhoneNumber:
    def create_phone_number(self, phone_number):
        return '({}{}{}) {}{}{}-{}{}{}{}' .format(*phone_number)


phone = PhoneNumber()
phone_number = phone.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print("New phone number: " + phone_number)