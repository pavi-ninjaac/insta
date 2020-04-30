"""
Find the output #3 (yield keyword)
"""
def mul(X):
     for loop in range(1,4):
          yield loop*X

a=mul(6)
for i in a:
     print(i,end=" ")
______________________
"""
A)6 12 18        B)[6, 12, 18]
C)error            D)0 6 12
ans: a
"""
