from pyModelChecking import *
from pyModelChecking.CTL import *

K = Kripke(R=[(0, 1), (1, 0), (1, 2), (2, 2),],
           L={0: set(['a']), 1: set(['a']), 2: set(['b'])})

# Print the formula
print("1", modelcheck(K,AG('a')))
print("2", modelcheck(K,EG('a')))
print("3", modelcheck(K,AF(EG('b'))))
print("6", modelcheck(K,EX('b')))
print("8", modelcheck(K,AU('b', 'a')))
print("9", modelcheck(K,AU('a', 'b')))
print("10", modelcheck(K,EU('a', 'b')))
