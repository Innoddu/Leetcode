def isValid(s):
        if len(s) == 1 or len(s) == 0:
            return False
        stack = []
        hashmap = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c in hashmap:
                if len(stack) > 0 and hashmap[c]== stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
     
        return False if len(stack) > 0 else True
