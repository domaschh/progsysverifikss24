from pyModelChecking import *
from pyModelChecking.CTLS import *

K = Kripke(R=[(0, 1), (1, 1), (1, 2), (2, 0)],
           L={0: set(['a']), 1: set(['b']), 2: set(['a'])})

phi = A(And('a', X('b')))
print(phi)
print(modelcheck(K, phi))

phi2 = Or((A(X('a'))), A(X('b')))
print(phi2)
print(modelcheck(K, phi2))