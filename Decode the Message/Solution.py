class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        dic = {}

        i = 97
        for letter in key:
            if letter not in dic:
                dic[letter] = chr(i)
                i += 1

        ans = ""
        for letter in message:
            if letter == " ":
                ans += " "
                continue
            ans += dic.get(letter)
        return ans
