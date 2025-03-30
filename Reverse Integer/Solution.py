class Solution:
    def reverse(self, x: int) -> int:
        word = ""
        string = str(x)
        low = -2**31
        up = 2**31 - 1

        if string[0] == '-':
            word += '-'

            for i in range(len(string)-1, 0, -1):
                word += string[i]
        else:
            for i in range(len(string)-1, -1, -1):
                word += string[i]

        if int(word) > low and int(word) < up:
            return int(word)
        else:
            return 0
        