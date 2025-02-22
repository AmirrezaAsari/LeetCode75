class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(word1, word2)
        result = ''
        len1 = len(word1)
        len2 = len(word2) # store them since we need them twice
        for i in range(max(len1, len2)):
            if (i == len1): 
                result += word2[i:]
                return result
            elif (i == len2):
                result += word1[i:]
                return result
            result += word1[i]
            result += word2[i]
        return result





print(Solution.mergeAlternately(Solution, "abc", "bqr"))