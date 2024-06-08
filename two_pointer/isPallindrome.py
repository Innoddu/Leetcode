def isPalindrome(self, s: str) -> bool:
        strs = ""
        lower_s = s.lower()

        for c in s:
            if c.isalnum():
                strs += c.lower()
        print(strs)
        return strs == strs[::-1]
