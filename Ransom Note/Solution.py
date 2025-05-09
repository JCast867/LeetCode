class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic2 = {}
        
        for letter in magazine:
            if letter not in dic2:
                dic2[letter] = 1
            else:
                dic2[letter] += 1

        for letter in ransomNote:
            if letter not in dic2:
                return False
            elif dic2[letter] == 0:
                return False
            else:
                dic2[letter] -= 1

        return True
    