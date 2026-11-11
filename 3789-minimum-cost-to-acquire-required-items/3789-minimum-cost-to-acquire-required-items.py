class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        
        option1 = need1 * cost1 + need2 * cost2
        # Both requirements using type 3
        option2 = max(need1, need2) * costBoth
        # Use type 3 for common requirements
        common = min(need1, need2)
        option3 = (common*costBoth+(need1-common)*cost1+(need2-common)*cost2)

        return min(option1, option2, option3)
        