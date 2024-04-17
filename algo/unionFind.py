class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x

    def get_groups(self):
        members = {}
        for member in range(self.n):
            p = self.find(member)        
            if members.get(p, False):
                members[p].append(member)
            else:
                members[p] = [member]

            # if members.get(self.find(member), -1) == -1:
            #     members[self.find(member)] = [member]
            # else:
            #     members[self.find(member)].append(member)
        return members
    
    def __str__(self):
        members = self.get_groups()
        return '\n'.join([f'parents: {member}, member: {members[member]}' for member in members])