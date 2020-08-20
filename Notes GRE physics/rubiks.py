import random
import time
from rubik import solve
from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves


SOLVED_CUBE_STR = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
MOVES = ["L", "R", "U", "D", "F", "B"]


def random_cube():
    """
    :return: A new scrambled Cube
    """
    scramble_moves = " ".join(random.choices(MOVES, k=200))
    a = Cube(SOLVED_CUBE_STR)
    a.X()
    a.sequence(scramble_moves)
    return a
a=random_cube()
#Imprime el cubo en forma canonica
#print(a)
#print("")
def removeNonAscii(s): return "".join(i for i in s if ord(i)<126 and ord(i)>32)
#imprime el scramble aleatorio en colores del cubo

scramble=removeNonAscii(str(a)).lower()
print(scramble)
print(Cube(scramble))
def organizar_scramble(scramble):
    string=scramble[:9]
    for i in range(1,5):
        for j in range (1,4):
            #i=1,j=1 k=9
            #i=1,j=2 k=21 = k+12
            #i=1,j=3 k=33 = k+12= k+2*12
            #i=2, j=1 k=12
            #i=2,j=2 k=24 =k+12
            k=9+3*(i-1)+12*(j-1)
            string+=scramble[k:k+3]
    string+=scramble[45:]
    return string
scramble=organizar_scramble(scramble)
M = {'b':'g', 'g':'b'}
STR = scramble
S = "".join([M.get(c,c) for c in STR])
scramble=S

print(scramble)
#Revisar scramble
def cont(scramble):
    return ("W:%s, O:%s, G:%s, R:%s, B:%s, Y:%s" %(scramble.count("w"),scramble.count("o"),scramble.count("g"),scramble.count("r"),scramble.count("b"),scramble.count("y")))
#print(cont(scramble))
print(cont(scramble))



from rubik_solver import utils
"""
print(utils.solve(cube, 'Beginner'))
print(utils.solve(cube, 'CFOP'))
"""
print(utils.solve(scramble, 'Kociemba'))
