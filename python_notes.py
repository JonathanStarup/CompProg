# copy-setup
import sys
INF = float('inf')
input = lambda: sys.stdin.readline().rstrip()
def iinput(): return list(map(int, input().split()))
def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))

# infinite
INF = float('inf')

# debug things
def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))

# Input
import sys
#def input(): return sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
def iinput(): return list(map(int, input().split()))

# unfold
lst = [1, 2, 3] 
print(*lst)

# reverse range (no allocation)
range(100)[::-1]

# memoization
import functools
@functools.lru_cache(maxsize=None)
def rec(x): 1 if x == 1 or x ==2 else rec(x-1) + rec(x-2)

# queues
from collections import deque
queue = deque()
queue.append(2)
queue.appendleft(2)
queue.popleft()
queue.pop()

# count things
from collections import Counter
cnt = Counter("DKLVFAHKLGASFLG")
cnt["A"]
cnt.most_common()
cnt.items()

from collections import defaultdict
d = defaultdict(lambda: "hej") # default value is "hej"

