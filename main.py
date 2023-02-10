import numpy as np
from math import pi, atan, atan2, atanh

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

    x = np.linalg.solve(a, b)
    ua, ub, uc = [i[0] for i in x]

    ur4 = ub - uc
    ir4 = g4 * ur4

    print(f"{iz=}")
    print(f"{g1=}")
    print(f"{g2=}")
    print(f"{g4=}")
    print(f"{g4=}")
    print(f"{g5=}")
    print(f"{x=}")
    print(f"{ua=}")
    print(f"{ub=}")
    print(f"{uc=}")
    print(f"{ur4=}")
    print(f"{ir4=}")

def problem_4(u1, u2, r1, r2, l1, l2, c1, c2, f):
    w = 2 * pi * f

    zl1 = complex(0, l1 * w)
    zl2 = complex(0, l2 * w)
    zc1 = complex(0, -1/(c1 * w))
    zc2 = complex(0, -1/(c2 * w))

    a = np.array([
        [r1 + zl1 + r2 + zl2, zl1 + r2, -zl2],
        [zl1 + r2, zl1 + r2 + zc1 + zc2, zc1],
        [-zl2, zc1, zc1 + zl2]
    ])

    b = np.array([
        [u1],
        [0],
        [u2]
    ])

    x = np.linalg.solve(a, b)
    ia, ib, ic = [i[0] for i in x]

    uc2: complex = zc2 * ib
    uc2_abs: complex = abs(uc2)

    oo = atan2(uc2.imag, uc2.real) * (180/pi)
    
    print(f"{w=}")
    print(f"{zl1=}")
    print(f"{zl2=}")
    print(f"{zc1=}")
    print(f"{zc2=}")
    print(f"{ia=}")
    print(f"{ib=}")
    print(f"{ic=}")
    print(f"{uc2=}")
    print(f"{uc2_abs=}")
    print(f"{oo=}")

def problem_5(u, l, r, i0):
    print('Not implemented yet')
