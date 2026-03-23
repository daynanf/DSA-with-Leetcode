class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for x in s:
            if not stack or x != "*":
                stack.append(x)
            elif x=="*":
                stack.pop()
        return "".join(stack)