class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {} # initilizes an empty dictionary, an unorderd collectioned of key value pairs being used to store key value paairs, also refferd to as an hashtable
        n = len(nums)
        for i in range(n): #iterate trough the array
            diff = target - nums[i] # for each element in nums, find the difference by subtracting it from the target number
            if diff in numdict: # checks if diff is in hash table, if it is we have a soloution if not add the elment nums[i] to the hashtable with its index as the value
                return [numdict[diff], i] #if diff exist in the hashmap that means a pair of elements that sums to the target has been found, numdict[diff] represents the index of the difference value. 
            numdict[nums[i]] = i
        return [] # if no solution found
