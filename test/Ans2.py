import io, os, sys
os.system("Cls")
with open("HandlInput.txt") as TxtOpen:
    INPUT = TxtOpen.read();
sys.stdin = io.StringIO(INPUT)

# ここにコードを貼り付ける
N = int(input())
A = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6)

Stack = []
def dfs(Stack):
  if len(Stack) == 1:
    return
  elif Stack[-1] != Stack[-2]:
    return 
  Stack.pop()
  Stack[-1] += 1
  dfs(Stack)

for a in A:
  Stack.append(a)
  dfs(Stack)
ans = len(Stack)
print(ans)