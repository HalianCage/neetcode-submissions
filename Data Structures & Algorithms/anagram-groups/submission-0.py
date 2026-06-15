class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        outputList = []

        while strs:

            anagramList = []
            freqMap = {}

            string = strs.pop(0)

            anagramList.append(string)

            for ch in string:
                freqMap[ch] = freqMap.get(ch, 0) + 1

            index = 0

            while index < len(strs):

                nextString = strs[index]
                freqMap2 = {}

                for ch in nextString:
                    freqMap2[ch] = freqMap2.get(ch, 0) + 1

                if freqMap2 == freqMap:
                    nextStringIndex = strs.index(nextString)
                    anagramList.append(strs.pop(nextStringIndex))
                    continue
                else:
                    index += 1

            outputList.append(anagramList)

        return outputList

