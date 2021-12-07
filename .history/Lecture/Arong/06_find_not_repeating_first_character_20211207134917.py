input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphaber_occurrence = alphabet_occurrence_array[arr_index]
        if alphaber_occurrence == 1:
            not_repeating_character_array.append(chr(index + ard("a")))

    print(not_repeating_character_array)
    return "_"


result = find_not_repeating_character(input)
print(result)