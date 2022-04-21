from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="040"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''4 5
1 2 10
1 2 1000
2 3 10000
2 3 100000
3 1 200000
4
1 0
2 10000
3 100000
4 0

'''
y = '''
'''
additional_case = [x]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
  N,M=map(int,input().split())
  bridge=[]
  for i in range(M):
    a,b,y=map(int,input().split())
    a-=1; b-=1
    bridge.append((a,b,y))
  Q=int(input())
  query=[]
  for i in range(Q):
    v,w=map(int,input().split())
    v-=1
    query.append((i,v,w))
  bridge.sort(key=lambda x: x[2])
  query.sort(reverse=True,key=lambda x: x[2])
  uf=UnionFind(N)
  ans=[0]*Q
  for i in range(Q):
    idx,c,y=query[i]
    while len(bridge)>0 and bridge[-1][2]>y:
      s,t,w=bridge.pop()
      uf.union(s,t)
    ans[idx]=uf.size(c)
  print(*ans,sep='\n')
  """ここから上にコードを記述"""

  print(test_case[__+1])