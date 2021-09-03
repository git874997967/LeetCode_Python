#1672. Richest Customer Wealth
def maximumWealth(accounts):
        maxAccount = 0
        for account in accounts:
            maxAccount = max(maxAccount,sum(account))
        return maxAccount