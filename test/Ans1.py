import io, os, sys
os.system("Cls")
with open("HandlInput.txt") as TxtOpen:
    INPUT = TxtOpen.read();
sys.stdin = io.StringIO(INPUT)

# ここにコードを貼り付ける
N = int(input())
P = list(map(int, input().split()))

def prev_permutatinon(P):
    for i in reversed(range(N - 1)):
        if P[i] < P[i + 1]:
            continue
        j = N - 1
        while P[i] < P[j]:
            j -= 1
        P[i], P[j] = P[j], P[i]
        return P[:i+1] + P[:i:-1]
    return False

print(*prev_permutatinon(P))