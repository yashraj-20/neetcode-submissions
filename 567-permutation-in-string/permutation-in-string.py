class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        
        need = Counter(s1)
        has = Counter(s2[:k])

        if need == has:
            return True
        
        for right in range(k, len(s2)):
            has[s2[right]] += 1
            left = s2[right - k]
            has[left] -= 1
            if has[left] == 0:
                del has[left]
            if has == need:
                return True
        return False