class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,2,3,3,4,4,5]
        
        hand.sort()
        count = Counter(hand)
        for num in hand:
            if count[num] != 0:
                for i in range(num, num+groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True