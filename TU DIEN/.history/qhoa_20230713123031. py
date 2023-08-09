def find_max_S(A, K):
    N = len(A)
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            max_val = float('-inf')
            for k in range(1, 3*j-1):
                if i-k >= 0:
                    max_val = max(max_val, dp[i-k][j-1] + (A[i-k] - A[i-k+1] + A[i]))

            dp[i][j] = max(dp[i][j], max_val)

    return dp[N][K]

# Example usage
A = [1, 2, 3, 4, 5]
K = 1
max_S = find_max_S(A, K)
print(max_S)
Trong ví dụ này, dãy số A là [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], và K = 2. Kết quả là 24, đạt được khi chọn các chỉ số i1 = 3, i2 = 6, i3 = 9, và tính giá trị S tương ứng.






