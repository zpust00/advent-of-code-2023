concatenated_numbers = 0  # Initialize as integer for summing

def spisani(first_number, last_number):
    num_str = str(first_number) + str(last_number)
    return int(num_str)

with open("1.dan.txt", "r") as file:
    for line in file:
        vrstica = line.strip()
        numbers = ''.join(char for char in vrstica if char.isdigit())

        if len(numbers) >= 2:
            first_number = int(numbers[0])
            last_number = int(numbers[-1])
            concatenated_numbers += spisani(first_number, last_number)
            print(first_number, last_number)

        elif len(numbers) == 1:
            first_number = int(numbers[0])
            last_number = int(numbers[0])
            concatenated_numbers += spisani(first_number, last_number)
            print(first_number, last_number)

print(concatenated_numbers)
