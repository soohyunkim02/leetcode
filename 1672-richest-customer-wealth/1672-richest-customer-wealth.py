class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for acc in accounts:
            wealth.append(sum(acc))
        result = max(wealth)
        return result