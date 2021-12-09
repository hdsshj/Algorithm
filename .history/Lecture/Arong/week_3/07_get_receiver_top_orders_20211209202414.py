top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]
# [0, 0, 0, 0, 0]
#  <- <- <- <- <-
#  6  9  5  7  4
# [0, 0, 0, 0, 4]

#  <- <- <- <-
#  6  9  5  7
# [0, 0, 0, 2, 4]

#  <- <- <-
#  6  9  5
# [0, 0, 2, 2, 4]

#  <- <-
#  6  9
#  [0, 0, 2, 2, 4]

#  <-
#  6
#  [0, 0, 2, 2, 4]


# [6, 9, 5, 7, 4]
# [0, 0, 0, 0, 4]
def get_receiver_top_orders(heights):
    # heights 라는 변수를 초기화 시킴
    answer = [0] * len(heights)  # [0, 0, 0, 0, 0]
    # heights가 빈 상태가 아닐때까지 반복문을 돌린다는 의미
    while heights:
        heights = heights.pop()
        # [6, 9, 5, 7]
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!