class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        for i in nums:
            if i in frequent:
                frequent[i] += 1
            else:
                frequent[i] = 1
        top_k = sorted(frequent, key= lambda k: frequent[k] , reverse = True)[0:k]
        return top_k
