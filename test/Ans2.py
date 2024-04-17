import io, os, sys
os.system("Cls")
with open("HandlInput.txt") as TxtOpen:
    INPUT = TxtOpen.read();
sys.stdin = io.StringIO(INPUT)

# ここにコードを貼り付ける
#　Kruskal法のアルゴリズムの本体
def kruskal(Edges, V, K):
    """
    入力
    Edges: (weight, (From_node, To_node))を管理するリスト
    V: 頂点数
    
    出力
    ans: 最小全域木の重み
    """
    Edges.sort() #重みが小さい順に辺をソートする

    ans = 0 #最小全域木の重み
    uf = UnionFind(V) #UnionFindを初期化. 初期は全頂点が異なるグループ
    for w, (From, To) in Edges:

        #同じグループ(木)に属する場合、その辺は無視する
        if uf.isSame(From, To):
            continue
        #異なるグループの場合、その辺を採用し、頂点From, Toを同じグループにする
        else:
            ans += (w % K)
            uf.unite(From, To)
    
    return ans

#=======以下、Union-Find木 各頂点の管理に利用===============
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]
        self.size = [1]*n
    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x]) #工夫2: 経路圧縮
            return self.parents[x]
    def isSame(self, x, y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            #なにもしない
            return
        #工夫1: サイズによる合併(小さい方を大き方に合併)
        if self.size[x] < self.size[y]:
            x, y = y, x #yが小さい方になるように交換する

        self.parents[y] = x #yの根をxに変更
        self.size[x] += self.size[y]

N, M, K = map(int, input().split())
Edges = []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    Edges.append((w, (u, v)))

ans = kruskal(Edges, N, K)
print(ans % K)