import math
def comb(n,r):  
    i = n - r
    return int((math.factorial(n))/(math.factorial(i)*math.factorial(r)))
def nbr_climbing(N):
    s=0;
    for i in range(N // 2 +1):
        s=s+comb(N-i,i)
    return s
def solution(A,B):
    result = [0] * len(A)
    for i in range(len(A)):
        result[i]= (nbr_climbing(A[i])& ((1 << B[i]) - 1))
    return result
