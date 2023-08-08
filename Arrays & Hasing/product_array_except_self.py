class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums)) #This line initializes a list called res with the length equal to the length of another list called nums. Each element of res is initially set to 1.

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #This line sets the value of the i-th element in the res list to the current value of prefix
            prefix *= nums[i] #This line multiplies the current value of prefix by the i-th element in the nums list. The updated value of prefix will be used in the next iteration of the loop.
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1): # This line starts a loop that will iterate over the indices of the elements in the nums list in reverse order.
            res[i] *= postfix #This line multiplies the current value of the i-th element in the res list by the current value of postfix
            postfix *= nums[i] #This line multiplies the current value of postfix by the i-th element in the nums list in reverse order. The updated value of postfix will be used in the next iteration of the loop.
        return res
