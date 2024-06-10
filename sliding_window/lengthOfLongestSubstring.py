def lengthOfLongestSubstring( s ):
        strs = ""
        maxLength = 0
        startPoint = 0
        idx = 0
        while idx < len(s):
            if s[idx] not in strs:
                strs += s[idx]
                maxLength = max(maxLength, len(strs))
                idx += 1
            else:
                startPoint = startPoint + 1
                idx = startPoint + 1
                maxLength = max(maxLength, len(strs))
                strs = ""
                strs += s[startPoint]
        return maxLength
