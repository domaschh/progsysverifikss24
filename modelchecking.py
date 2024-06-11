from pyModelChecking import *
from pyModelChecking.CTLS import *

K = Kripke(R=[(0, 1), (1, 0), (1, 2), (2, 2)],
           L={0: set(['a']), 1: set(['a']), 2: set(['b'])})

# Print the formula
p1 = A(G('a'))
print("1",p1, modelcheck(K, p1))
p2 = E(G('a'))
print("2",p2, modelcheck(K, p2))
p3 = A(F(G('b')))
print("3",p3, modelcheck(K, p3))
p4 = A(F(E(G('b'))))
print("4",p4, modelcheck(K, p4))
p5 = E(F(G('b')))
print("5",p4, modelcheck(K, p5))
p6 = E(X('b'))
print("6",p4, modelcheck(K, p6))
p7 = E(G(F('a')))
print("7",p7, modelcheck(K, p7))
p8 = A(U('b','a'))
print("8",p8, modelcheck(K, p8))
p9 = A(U('a','b'))
print("9",p9, modelcheck(K, p9))
p10 = E(U('a','b'))
print("9",p10, modelcheck(K, p10))

