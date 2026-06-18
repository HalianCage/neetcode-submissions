class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}
        '''
        1: 1,
        2: 2,
        3: 3
        '''

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1

        count = [[] for _ in range(len(nums)+1)]

        # insert list inside each corresponding index of the count list
        for key, val in freqMap.items():
                count[val].append(key)

        output = []
        i = -1
        while len(output) != k:

            for n in count[i]:
                output.append(n)
                if len(output) == k:
                    return output

            i -= 1

        return output
