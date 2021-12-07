input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
  count_all_zero = 0
  count_all_one = 0
  
  if string[0] == '1' : # 시작 문자가 1이면 0으로 바꾸는 카운터 1 증가
    count_all_zero += 1 
  if string[0] == '0' : # 시작 문자가 0이면 1로 바꾸는 카운터 1 증가
    count_all_one += 1
    
  for i in range(len(string) - 1) :
    if string[i] != string[i+1] : 
      if string[i+1] == '0' :
        count_all_one += 1
      if string[i+1] == '1' :
        count_all_zero += 1
  return min(count_all_one, count_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)