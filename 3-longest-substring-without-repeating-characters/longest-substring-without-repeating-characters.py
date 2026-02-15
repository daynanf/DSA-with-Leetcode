class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=""
        ans=0
        for i in range(len(s)):
            if s[i] not in a:
                a+=s[i]

            else:
                ans=max(len(a),ans)
                while s[i] in a:
                    a=a[1:]
                a+=s[i]
        ans = max(len(a), ans)
        return ans 

