def solution(A):
    for i in range(len(A)):
        A[i] = abs(A[i])
    dp = [False] * (sum(A) + 1)
    dp[0] = True
    for i in range(len(A)):
        for j in reversed(range(0, sum(A) + 1)):
            if dp[j] and dp[j + A[i]] <= sum(A):
                dp[j + A[i]] = True
    min_v = sum(A)
    for i in range(sum(A) // 2 + 1):
        if dp[i] == 1:
            P = i
            Q = sum(A) - P
            min_v = min(min_v, Q - P)
    return min_v
