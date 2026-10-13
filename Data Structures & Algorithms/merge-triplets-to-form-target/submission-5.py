class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # x_max = triplets[0][0]
        # y_max = triplets[0][1]
        # z_max = triplets[0][2]
        # if len(triplets) == 1 and [x_max, y_max, z_max] == target:
        #     return True

        x_max = -1
        y_max = -1
        z_max = -1

        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            x_max = max(x_max, triplets[i][0])
            y_max = max(y_max, triplets[i][1])
            z_max = max(z_max, triplets[i][2])

            if [x_max, y_max, z_max] == target:
                return True
        
        return False