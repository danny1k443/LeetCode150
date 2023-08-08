class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: #takes in a list of intergers called nums and returns a boolean value
        hset = set() # creats an empty set, sets are unordered elements with no duplicates
        for i in nums: # iterate over each element in the num list
            if i in hset: # checks if the current element i already exists in the hset
                return True #if found in the hset return true,  a duplicate found
            hset.add(i) # adds the current element i into the hset, this will ensure we can detect a second occuracne of the same element
        return False #if the for loops completes without any duplicates return false
