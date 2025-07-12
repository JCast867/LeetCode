class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ""
        for char in s:
            if char.isalnum():
                final += char
        final = final.lower()
        
        left = 0
        right = len(final) - 1
        print(final)

        while left < right:
            if final[left] != final[right]:
                return False
            left += 1
            right -= 1

        return True
