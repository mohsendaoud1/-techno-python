def solution(N,A):
    result = [0] * N
    for i in range(len(A)):
        if(A[i]<N):
            result[A[i]-1]=result[A[i]-1]+1
        elif(A[i]==N+1):
            result = [max(result)] * N
    return result
