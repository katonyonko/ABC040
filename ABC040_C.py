from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="040"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''9
314 159 265 358 979 323 846 264 338
'''
y = '''
'''
additional_case = [x]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  A=list(map(int,input().split()))
  cost=[10**10]*N
  cost[0]=0
  for i in range(N-1):
    if i<N-2: cost[i+2]=min(cost[i+2],cost[i]+abs(A[i+2]-A[i]))
    cost[i+1]=min(cost[i+1],cost[i]+abs(A[i+1]-A[i]))
  print(cost[-1])
  """ここから上にコードを記述"""

  print(test_case[__+1])