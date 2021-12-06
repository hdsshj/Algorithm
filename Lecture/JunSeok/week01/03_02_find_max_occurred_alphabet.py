input = "hello my name is sparta"


# 최대로 빈도수가 많았던 알파벳 가져오기

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)  # 알파벳을 가지고싶어
    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)

# 아스키코드 구글링 python number to char 검색
# a->0
# a-> ord(a) -> 97 - ord(a) = 0
# 0 -> a
# 0 -> 0 + ord(a) -> 97 -> chr(97) -> a
