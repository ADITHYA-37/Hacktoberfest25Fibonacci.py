def fibonacci(n):
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]  # ❌ IndexError for last element
print(fibonacci(6))  # Expected 8
