import itertools

n = 3
S = ["choku", "dai", "sann"]

t = sum(len(s) for s in S)
t += n - 1
t = 16 - t
for T in itertools.permutations(S):
    X = []
    
    def dfs(i, t):
        X.append(T[i])
        if i == n - 1:
            X.pop()
            return

        for j in range(t + 1):
            X.append("_")
            dfs(i + 1, t - j)
        for _ in range(t + 2):
            X.pop()


    dfs(0, t)

print(-1)