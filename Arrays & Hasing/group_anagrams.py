class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list) # default hashmap, where the default value is a list. 
         # automatically initializes a default value for a nonexistent key. in this case an empty list, this will be used to store anagrams, the sorted word will be the key and the and the orignal word will be appedned to the list

        for word in strs:
            count = [0] * 26 # making an array of 26 zeros in it, 26 zeros one for each character from a to z
            for i in word: # go thorugh every single character in each string
                count[ord(i) - ord("a")] += 1 #to map a to index 0 and z to index 25, by subtracting the ascii value of whatever charater we are at minus the ascii value of a. 
                #lower case a - lower case a = 0, lowercase z - lowercase a = 25
                # =+1 increment by one to count how many characters we have
            answer[tuple(count)].append(word)

        return answer.values() # returns the values in the dictionary, the anagrams grouped together
