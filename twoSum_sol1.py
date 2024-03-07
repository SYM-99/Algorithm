class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(length):
            tmp1 = target - nums[i]
            for j in range(length-1):
                tmp2 = tmp1 - nums[j+1]
                if tmp2 == 0 and i != j+1:
                    ans.append(i)
                    ans.append(j+1)
                    return ans
                else:
                    continue
