
# def checker(i, len):
#     i = i
#     while i < len:
#         i + 1

# def sum(num_1, num_2):
#     return num_1 + num_2

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        k = i
        l = k + 1
        while l <= len(nums) - 1:
            sum = nums[i] + nums[l]
            print(sum)
            if sum == target:
                return [i, l]
            l = l + 1
            
print(twoSum(nums = [2,7,11,15], target = 9))


print(twoSum(nums = [3,2,4], target = 6))

print(twoSum(nums = [3,3], target = 6))