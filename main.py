import numpy as np
from argparse import ArgumentParser

values = [
    {
        'A': (80,  120, 350, 650, 410, 130, 360, 750, 310, 190),
        'B': (95,  115, 650, 730, 340, 330, 410, 830, 340, 220),
        'C': (100, 80,  450, 810, 190, 220, 220, 720, 260, 180),
        'D': (105, 85,  420, 980, 330, 280, 310, 710, 240, 200),
        'E': (115, 55,  485, 660, 100, 340, 575, 815, 255, 225),
        'F': (125, 65,  510, 500, 550, 250, 300, 800, 330, 250),
        'G': (130, 60,  380, 420, 330, 440, 450, 650, 410, 275),
        'H': (135, 80,  680, 600, 260, 310, 575, 870, 355, 265),
    },
    {
        'A': (50,  100, 525, 620, 210, 530, 100),
        'B': (100, 50,  310, 610, 220, 570, 200),
        'C': (200, 70,  220, 630, 240, 450, 300),
        'D': (150, 200, 200, 660, 200, 550, 400),
        'E': (250, 150, 335, 625, 245, 600, 150),
        'F': (130, 180, 350, 600, 195, 650, 250),
        'G': (180, 250, 315, 615, 180, 460, 350),
        'H': (220, 190, 360, 580, 205, 560, 180),
    },
    {
        'A': (120, 0.9,  0.7,  53, 49, 65, 39, 32),
        'B': (150, 0.7,  0.8,  49, 45, 61, 34, 34),
        'C': (110, 0.85, 0.75, 44, 31, 56, 20, 30),
        'D': (115, 0.6,  0.9,  50, 38, 48, 37, 28),
        'E': (135, 0.55, 0.65, 52, 42, 52, 42, 21),
        'F': (145, 0.75, 0.85, 48, 44, 53, 36, 25),
        'G': (160, 0.65, 0.45, 46, 41, 53, 33, 29),
        'H': (130, 0.95, 0.50, 47, 39, 58, 28, 25),
    },
    {
        'A': (35, 55, 12, 14, 120*10**-3, 100*10**-3, 200*10**-6, 105*10**-6, 70),
        'B': (25, 40, 11, 15, 100*10**-3, 85*10**-3,  220*10**-6, 95*10**-6,  80),
        'C': (35, 45, 10, 13, 220*10**-3, 70*10**-3,  230*10**-6, 85*10**-6,  75),
        'D': (45, 50, 13, 15, 180*10**-3, 90*10**-3,  210*10**-6, 75*10**-6,  85),
        'E': (50, 30, 14, 13, 130*10**-3, 60*10**-3,  100*10**-6, 65*10**-6,  90),
        'F': (20, 35, 12, 10, 170*10**-3, 80*10**-3,  150*10**-6, 90*10**-6,  65),
        'G': (55, 50, 13, 12, 140*10**-3, 60*10**-3,  160*10**-6, 80*10**-6,  60),
        'H': (65, 60, 10, 10, 160*10**-3, 75*10**-3,  155*10**-6, 70*10**-6,  95),
    },
    {
        'A': (40, 50, 10, 16),
        'B': (30, 10, 20, 15),
        'C': (35, 5,  30, 14),
        'D': (25, 5,  25, 12),
        'E': (40, 30, 40, 11),
        'F': (22, 30, 15, 10),
        'G': (20, 50, 25, 8 ),
        'H': (18, 50, 40, 5 ),
    }
]

def problem_1(u1, u2, r1, r2, r3, r4, r5, r6, r7, r8):
    u = u1 + u2
    print(f"{u=}")

    r23 = (r2 * r3) / (r2 + r3)
    r68 = r6 + r8
    print(f"{r23=}")
    print(f"{r68=}")

    d = r23 + r4 + r5
    ra = (r23 * r4) / d
    rb = (r23 * r5) / d
    rc = (r4 * r5) / d
    print(f"{ra=}")
    print(f"{rb=}")
    print(f"{rc=}")

    r1a = r1 + ra
    rb68 = rb + r68
    rc7 = rc + r7
    rb68c7 = (rb68 * rc7) / (rb68 + rc7)
    rekv = r1a + rb68c7
    i = u / rekv
    print(f"{r1a=}")
    print(f"{rb68=}")
    print(f"{rc7=}")
    print(f"{rb68c7=}")
    print(f"{rekv=}")
    print(f"{i=}")

    ur1 = i * r1
    urb68c7 = i * rb68c7
    irb68 = urb68c7 / rb68
    ur68 = irb68 * r68
    ur2 = u - ur1 - ur68
    ir2 = ur2 / r2
    print(f"{ur1=}")
    print(f"{urb68c7=}")
    print(f"{irb68=}")
    print(f"{ur68=}")
    print(f"{ur2=}")
    print(f"{ir2=}")

def problem_2(u, r1, r2, r3, r4, r5, r6):
    r123 = r1 + r2 + r3
    ri = (r123 * r4) / (r123 + r4)

    rekv = r1 + r3 + r2 + r4
    ix = u / rekv
    
    ui = r4 * ix

    ir5 = ui / (ri + r5)
    ur5 = ir5 * r5

    print(f"{r123=}")
    print(f"{ri=}")
    print(f"{rekv=}")
    print(f"{ix=}")
    print(f"{ui=}")
    print(f"{ir5=}")
    print(f"{ur5=}")

def problem_3(u, i1, i2, r1, r2, r3, r4, r5):
    iz = u / r1

    g1 = 1/r1
    g2 = 1/r2
    g3 = 1/r3
    g4 = 1/r4
    g5 = 1/r5

    a = np.array([
        [-g1 - g2 - g3, g2, 0],
        [g2, -g2 - g4, g4],
        [0, g4, -g4 - g5]
    ])

    b = np.array([
        [-iz],
        [i2],
        [i1 - i2]
    ])

    x = np.linalg.solve(a, b)
    ua, ub, uc = [i[0] for i in x]

    ur4 = ub - uc
    ir4 = g4 * ur4

    print(f"{iz=}")
    print(f"{g1=}")
    print(f"{g2=}")
    print(f"{g3=}")
    print(f"{g4=}")
    print(f"{g5=}")
    print(f"{ua=}")
    print(f"{ub=}")
    print(f"{uc=}")
    print(f"{ur4=}")
    print(f"{ir4=}")
    print(f"{x=}")

    a = np.array([
        [-g1 - g2 - g3, g2, 0],
        [g2, -g2 - g4, g4],
        [0, g4, -g4 - g5]
    ])

    b = np.array([
        [-iz],
        [i2],
        [i1 - i2]
    ])
    print(f"{-g1 - g2 - g3=}")
    print(f"{-g2 - g4=}")
    print(f"{-g4 - g5=}")
    print(f"{-iz=}")
    print(f"{i1 - i2=}")

def problem_4(u1, u2, r1, r2, l1, l2, c1, c2, f):
    print('Not implemented yet')

def problem_5(u, l, r, i0):
    U = 8
    L = 50
    R = 40
    T = 0
    START = 4

    K_d = U / L * e ** (-R/L * T)
    K_d = U / L * e ** (-R/L * T)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Solve electrical circuits problems for my university course."
    )

    parser.add_argument(
        "groups",
        type=str,
        help="Example: AACBD"
    )

    parser.add_argument(
        "problem",
        type=int,
        nargs="?",
        help="Problem number. Example: 1. If empty, then all problems will be solved."
    )

    solutions = [problem_1, problem_2, problem_3, problem_4, problem_5]
    args = parser.parse_args()

    groups = args.groups.upper()[:5]


    if args.problem:
        solutions[args.problem - 1](*values[groups[args.problem - 1]])
    else:
        for i in range(5):
            solutions[i](*values[groups[i]])
