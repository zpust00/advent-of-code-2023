concatenated_numbers = 0

word_to_number = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def spisani(first_number, last_number):
    num_str = str(first_number) + str(last_number)
    return int(num_str)

def besede_v_stevilke(text):
    i = 0
    result = []
    while i < len(text):
        for word, number in word_to_number.items():
            if text[i:i+len(word)] == word:
                result.append(number)
                i += len(word)
                break
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)


with open("1.dan.txt", "r") as file:
    for line in file:
        vrstica = line.strip()
        vrstica = besede_v_stevilke(vrstica)
        numbers = ''.join(char for char in vrstica if char.isdigit())

        if len(numbers) >= 2:
            first_number = int(numbers[0])
            last_number = int(numbers[-1])
            concatenated_numbers += spisani(first_number, last_number)
            print(spisani(first_number, last_number))

        elif len(numbers) == 1:
            first_number = int(numbers[0])
            last_number = int(numbers[0])
            concatenated_numbers += spisani(first_number, last_number)
            print(spisani(first_number, last_number))

print(concatenated_numbers)
