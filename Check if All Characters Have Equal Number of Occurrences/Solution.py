class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        num = list(dic.values())[0]
        for i in dic:
            if dic[i] != num:
                return False

        return True