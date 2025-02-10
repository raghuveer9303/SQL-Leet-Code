class Solution:
    def clearDigits(self, s: str) -> str:
        string = ''
        for char in s:
            if not char.isnumeric():
                string = string + char
            else:
                string = string[:-1]

        if string == s:
            return string
        return self.clearDigits(string)
        