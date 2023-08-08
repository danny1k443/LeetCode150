class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #check if the two strings are the same length if not return false
            return False
        for i in set(s): # iterates of the charactes in set s the set ensures that the character is considerd only onces
            if s.count(i) != t.count(i):# for each unique character in s, line checks if the count of characters in s is diffrent from the count of characters in t, if count differs return false
            #count() method returns the number of times the element i appears in the sequence
                return False 
        return True #has to be outside the for loop becasue we want the loop to run completly and after a complete run return true if the count is the same
