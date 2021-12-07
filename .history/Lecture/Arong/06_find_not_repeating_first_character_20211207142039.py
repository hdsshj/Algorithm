input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    # 반복되지 않는 값들을 넣는 변수
    not_repeating_character_array = []
    # alphabet_occurrence_array 길이 만큼 반복!
    for index in range(len(alphabet_occurrence_array)):
        # 각 알파벳 빈도가 개장됨
        alphabet_occurrence = alphabet_occurrence_array[arr_index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    print(not_repeating_character_array)

    # 알파벳 순서대로 나오게 하지 않기 위해 입력한 문자열을 대상으로 반복문 다시 돌림
    for char in string:
        if char in not_repeating_character_array:
            # 바로 반환되게 해줌
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)