# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         s_len = len(s)
#         t_len = len(t)
#         start = end = 0
#         minlen = 10**9
#         res = ""

#         cnt = 0

#         counter = {ch: 0 for ch in s}

#         for ch in t:
#             if ch not in counter:
#                 return res
#             counter[ch] += 1
        
#         while end < s_len:
#             counter[s[end]] -= 1
            
#             if s[end] in counter and counter[s[end]] > 0:
#                 cnt += 1
            
#             while cnt == t_len:
#                 if end-start+1 < minlen:
#                     res = s[start:end]
#                 counter[s[start]] += 1
#                 start += 1
#                 if counter[s[start]] > 0:
#                     cnt -= 1
            
#             end += 1
#         return res
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        counter = {ch: 0 for ch in t}

        for ch in t:
            counter[ch] += 1

        start = 0
        cnt = 0
        minlen = float('inf')
        res = ""

        for end in range(len(s)):
            if s[end] in counter:
                counter[s[end]] -= 1

                if counter[s[end]] >= 0:
                    cnt += 1

            while cnt == len(t):
                if end - start + 1 < minlen:
                    minlen = end - start + 1
                    res = s[start:end+1]

                if s[start] in counter:
                    counter[s[start]] += 1

                    if counter[s[start]] > 0:
                        cnt -= 1

                start += 1

        return res