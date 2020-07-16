# Name:         Roger Silva Santos Aguiar
# Function:     It takes an integer as input, and returns the number
#               of bits that are equal to one in the binary representation
#               of that number.
# Initial date: July 16, 2020
# Last update:  July 16, 2020

class BitCounting:
    def count_bits_equal_one(self, number):
        binary_representation = []
        bits_equal_one = 0

        while int(number != 1):
            binary_representation.append(int(number % 2))
            if int(number % 2) == 1:
                bits_equal_one = bits_equal_one + 1

            number = int(number / 2)
        if number == 1:
            binary_representation.append(1)
            bits_equal_one = bits_equal_one + 1

        binary_representation_number = self.display_binary_representation(binary_representation)
        print("The number that you entered has {} bits equal 1.".format(bits_equal_one))
        print("Binary representation: {}" .format(binary_representation_number))

        return bits_equal_one

    def display_binary_representation(self, binary_representation = []):
        binary_representation_number = ''

        for bit in binary_representation:
            binary_representation_number = str(bit) + binary_representation_number

        return binary_representation_number

if __name__ == '__main__':
    bit = BitCounting()

    number = int(input("Enter an integer number: "))
    bit.count_bits_equal_one(number)

