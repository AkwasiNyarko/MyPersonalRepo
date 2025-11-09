class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if stack:
                    if mapping[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0