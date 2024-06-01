# 1899. Merge Triplets to Form Target Triplet
def mergeTriplets(triplets, target):
        i, j, k = target[0], target[1], target[2]
        res = []
        for x, y, z in triplets:
            if x <= i and y <= j and z <= k:
                x = i - x 
                y = j - y
                z = k - z
                if x == 0:
                    target[0] = 0
                if y == 0:
                    target[1] = 0
                if z == 0:
                    target[2] = 0
        if sum(target) == 0:
            return True
        return False
