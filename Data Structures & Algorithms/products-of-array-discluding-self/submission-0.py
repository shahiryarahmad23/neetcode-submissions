class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        for i in range(len(output)):
            output[i] = pre
            pre *= nums[i]
        post = 1
        for j in range(len(output) - 1, -1,-1):
            output[j] *= post
            post *= nums[j]
        return output

        