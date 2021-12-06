input = [3, 5, 6, 1, 2, 4]


# 입력값의 분포에 따라서 성능이 변할 수 있다.

def is_number_exist(number, array):
    for element in array:  # array 의 길이만큼 아래 연산이 실행
        if number == element:  # 비교연산 1번 실행
            return True  # N * 1 = N 만큼의 시간복잡도가 걸렸다.

    return False


result = is_number_exist(3, input)
print(result)

# 빅오 표기법 O(N) / 빅 오메가 오메가(1)
# 알고리즘에서는 거의 모든 알고리즘을 빅오 표기법으로 분석한다.
# 왜냐 대부분의 입렵값이 최선의 경우일 가능성은 굉장히 적을 뿐더러, 우리는 최악의 경우를 대비해야 하기 떄문이다.
