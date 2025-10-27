def fibonacci_sequence(num_terms):
    if num_terms <= 0:
        return []
    elif num_terms == 1:
        return [0]
    # Create dp list to hold all Fibonacci numbers up to num_terms
    dp = [0] * num_terms
    dp[0] = 0
    dp[1] = 1
    for i in range(2, num_terms):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp

# Take input from user
n = int(input("Enter the number of Fibonacci terms to print: "))
fib_seq = fibonacci_sequence(n)
print("Fibonacci sequence:")
print(' '.join(str(num) for num in fib_seq))
