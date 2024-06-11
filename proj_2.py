from z3 import *

def main():
    # initialize Z3
    s = Solver()

    n = 6 # Feel free to choose other values as well (tip: n = 6 has 4 solutions; n = 7 has 40)

    # define the variables
    queenConstants = [Int(f'q{i}') for i in range(n)]

    # add the constraints
    # Each queen must be in a different column
    s.add([And(queenConstants[i] >= 0, queenConstants[i] < n) for i in range(n)])

    # No two queens can be in the same column
    s.add(Distinct(queenConstants))

    # No two queens can be in the same diagonal
    s.add([If(i != j, queenConstants[i] - queenConstants[j] != i - j, True) for i in range(n) for j in range(n)])
    s.add([If(i != j, queenConstants[i] - queenConstants[j] != j - i, True) for i in range(n) for j in range(n)])

    # enumerate all solutions
    solCnt = 0

    while s.check() == sat:
        # output the solution
        model = s.model()
        for i in range(n):
            print("{} = {};".format(queenConstants[i], model[queenConstants[i]].as_long()), end=" ")
        print()

        # block the current solution
        block = []
        for i in range(n):
            block.append(queenConstants[i] != model[queenConstants[i]])
        s.add(Or(block))

        solCnt += 1

    print("Total number of solutions: {}".format(solCnt))

main()
