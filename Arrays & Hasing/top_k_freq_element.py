#solution 1 better to understand
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap will be used to count the occunaces of each value
        freq = [[] for i in range(len(nums) + 1)] # empty array about the size of our input + 1
        for n in nums: # go trough every value in nums 
            count[n] = 1 + count.get(n,0) # counting how many times it occurs, defalut value of zero if it doesnt exist yet
        for n, c in count.items():#this is gonna return every signal key value pair, for every number and count in the key value pair
            freq[c].append(n) #append to the list n, saying that this value n occurs this amount of time

        res = []
        for i in range(len(freq) - 1, 0, -1): # iterating trough the array frwq in decending order
        # len(freq) - 1 is the last index, all the way up till 0, and were going in desending order hence the -1
            for n in freq[i]:# n at this index i
                res.append(n) # take that n value and append it to our result. 
                if len(res) == k:
                    return res






#solution 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) #Counter counts the number of occurance of elements in the nums list
        heap = [] # initilize and empty lists named heap
        
        for num, freq in counter.items(): 
            #counter.items() is a way to access the elements and their corresponding counts in the counter container. It returns a collection of pairs, where each pair consists of an element and its count
            #The line for num, freq in counter.items(): sets up a loop that iterates over each pair in the collection of elements and counts.
            #In each iteration of the loop:num represents the current element being considered. It could be any number from the original list of numbers.freq represents the count of how many times the current element (num) appears in the original list.
            heapq.heappush(heap, (-freq, num)) # pushes a tuple This line pushes a tuple (-freq, num) onto the heap list. The tuple contains the negative frequency (-freq) as the primary key and the number (num) as the secondary key. By negating the frequency,creating a min-heap based on the frequency, where the elements with the lowest frequencies will be at the top.
        
        result = [] #create an empty list called results 
        for _ in range(k): # for loops runs k times  the underscore _ is used as a placeholder when we dont need to use a varible to run the for loop
            result.append(heapq.heappop(heap)[1]) #  In each iteration, the code pops the smallest tuple from the heap using heapq.heappop. It retrieves the number ([1] index of the tuple) and appends it to the result list.
            #fter the for loop completes, the result list contains the top k frequent elements
        
        return result
