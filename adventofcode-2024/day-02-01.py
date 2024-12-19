def is_safe(nums):
    delta_nums = [abs(nums[i+1] - nums[i]) for i in range(len(nums)-1)]
    sub_delta_nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]


    if max(delta_nums) > 3:
        return False
    if all([x > 0 for x in sub_delta_nums]) or all([x < 0 for x in sub_delta_nums]):
        pass
    else:
        return False
    return True

if __name__ == '__main__':
    list_of_nums = []
    with open('input_day_2.txt', 'r') as f:
        lines = f.read().splitlines(True) 
        for line in lines:
            list_of_nums.append([int(x) for x in line.split(' ')])
    safe_list = [x for x in list_of_nums if is_safe(x)]
    print(len(safe_list))
    
