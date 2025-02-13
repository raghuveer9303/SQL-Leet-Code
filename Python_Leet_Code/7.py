class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x<0:
            x_str = x_str[1:]
            output = int(f"-{x_str[::-1]}")
            if output > (-2^31):
                return 0
            else:
                return output

        else:
            output = int(x_str[::-1])
            if output <(2^31 - 1):
                return 0
            else:
                return output


sol = Solution()
print(sol.reverse(123))