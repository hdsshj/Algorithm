finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # index값
    count = 0
    min_num = 0
    max_num = len(array) - 1
    search_num = (min_num + max_num) // 2
    
    while min_num <= max_num :
      count += 1
      if array[search_num] == target :
        print('is count', count)
        return True
      elif array[search_num] > target :
        max_num = search_num - 1
      else :
        min_num = search_num + 1
      search_num = (max_num + min_num) // 2
    # 구현해보세요!
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)