input = "hello my name is sparta"


# 각 알파벳마다 문자열을 돌면서 몇글자가 나오는지 확인하는 방법

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                      "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:    # for 문 이용해서 알파벳을 하나하나 꺼내서
        occurrence = 0
        for char in string:            # 문자열에 있는 문자와 동일 하다면
            if char == alphabet:
                occurrence += 1        # occurrence 를 하나씩 증가시켜

        if occurrence > max_occurrence:  # max_occurrence 를 업데이트 하는 방식
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
