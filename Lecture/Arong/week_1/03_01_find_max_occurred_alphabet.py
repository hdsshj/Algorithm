input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "s", "y", "z"
    ]

    # 최고로 많이 나온 횟수를 저장하기 위한 변수
    max_occurrence = 0
    # 최고로 많이 나왔던 알파벳을 저장하기 위한 변수
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)