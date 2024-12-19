def can_be_safe(nums):
    # what element can be remove to make it safe?
    # remove a position and check if the list is safe
    for i in range(len(nums)):
        new_list = nums[:i] + nums[i+1:]
        if safe_first_rule(new_list) and safe_second_rule(new_list):
            return True
    return False

def safe_first_rule(nums):
    delta_nums = [abs(nums[i+1] - nums[i]) for i in range(len(nums)-1)]

    if not delta_nums or max(delta_nums) > 3:
        return False
    return True

def safe_second_rule(nums):
    sub_delta_nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    if all([x > 0 for x in sub_delta_nums]) or all([x < 0 for x in sub_delta_nums]):
        return True
    return False


def is_safe(nums):
    if safe_first_rule(nums) and safe_second_rule(nums):
        return True
    return can_be_safe(nums)

if __name__ == '__main__':
    list_of_nums = []
    with open('input_day_2.txt', 'r') as f:
        lines = f.read().splitlines(True) 
        for line in lines:
            list_of_nums.append([int(x) for x in line.split(' ')])
    safe_list = [x for x in list_of_nums if is_safe(x)]
    print(len(safe_list))
    
