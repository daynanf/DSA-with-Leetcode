class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        ans="/"
        command=path.split("/")
        for x in command:
            if x=="":
                continue
            elif (x!="." and x!=".." ):
                stack.append(x)
            elif x==".." and stack:
                stack.pop()
        for s in stack:
            ans+=s+"/"
        return ans[:-1:1] if ans[:-1:1] else ans 