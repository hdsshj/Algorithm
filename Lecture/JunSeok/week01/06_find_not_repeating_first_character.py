# 문제
# 다음과 같이 영어로 되어있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환 하시오
# 만약 그런 문자가 없다면 _를 반환하시오
# "abadabac" 반복되지 않는 문자는 d,c가 있지만 "첫번째" 문자니까 d 를 반환해주면 된다

input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26                # 배열

    for char in string:                                 # 문자열 하나하나 돌면서
        if not char.isalpha():                          # char 가  알파벳 아니면 버리고 알파벳이면
            continue
        arr_index = ord(char) - ord("a")                # array index 로 변환 한다. 어떻게? 아스키 코드로
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):                     # 알파벳의 길이만큼 반복
        alphabet_occurrence = alphabet_occurrence_array[index]              # index 의 값을 빼서 오큐런스에 저장
        if alphabet_occurrence == 1:                                        # 빈도수가 1일 때
            not_repeating_character_array.append(chr(index + ord("a")))     # 해당 알파벳을 넣어준다. (index 를 다시한번 알파벳으로 전환 해줘야함)

    print(not_repeating_character_array)    # 기존 문자열의 순서를 보장해주지 않는다.

    for char in string:
        if char in not_repeating_character_array:
            return char                                       # 이렇게 해줘야 현재 들어온 문자열의 순서에 맞게 반환을 해줄수 있다.
    return "_"


result = find_not_repeating_character(input)
print(result)