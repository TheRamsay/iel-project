import numpy as np

def first():
    U = 170
    R1 = 485.0
    R2 = 660.0
    R3 = 100.0
    R4 = 340.0
    R5 = 575.0
    R6 = 815.0
    R7 = 255.0
    R8 = 225.0

    R23 = (R2 * R3) / (R2 + R3)
    R68 = R6 + R8
    print(f"{R23=}")
    print(f"{R68=}")

    D = R23 + R4 + R5
    RA = (R23 * R4) / D
    RB = (R23 * R5) / D
    RC = (R4 * R5) / D
    print(f"{RA=}")
    print(f"{RB=}")
    print(f"{RC=}")

    R1A = R1 + RA
    RB68 = RB + R68
    RC7 = RC + R7
    RB68C7 = (RB68 * RC7) / (RB68 + RC7)
    REKV = R1A + RB68C7
    I = U / REKV
    print(f"{R1A=}")
    print(f"{RB68=}")
    print(f"{RC7=}")
    print(f"{RB68C7=}")
    print(f"{REKV=}")
    print(f"{I=}")

    UR1 = I * R1
    URB68C7 = I * RB68C7
    IRB68 = URB68C7 / RB68
    UR68 = IRB68 * R68
    UR2 = U - UR1 - UR68
    IR2 = UR2 / R2
    print(f"{UR1=}")
    print(f"{URB68C7=}")
    print(f"{IRB68=}")
    print(f"{UR68=}")
    print(f"{UR2=}")
    print(f"{IR2=}")


def second():
    U = 220
    R1 = 190
    R2 = 360
    R3 = 580
    R4 = 205
    R5 = 560

    R123 = R1 + R2 + R3
    RI = (R123 * R4) / (R123 + R4)

    REKV = R1 + R3 + R2 + R4
    IX = U / REKV
    
    UI = R4 * IX

    IR5 = UI / (RI + R5)
    UR5 = IR5 * R5

    print(f"{R123=}")
    print(f"{RI=}")
    print(f"{REKV=}")
    print(f"{IX=}")
    print(f"{UI=}")
    print(f"{IR5=}")
    print(f"{UR5=}")


def third():
    U = 115
    I1 = 0.6
    I2 = 0.9
    R1 = 50
    R2 = 38
    R3 = 48
    R4 = 37
    R5 = 28

    IZ = U / R1

    G1 = 1/R1
    G2 = 1/R2
    G3 = 1/R3
    G4 = 1/R4
    G5 = 1/R5

    A = np.array([
        [-G1 - G2 - G3, G2, 0],
        [G2, -G2 - G4, G4],
        [0, G4, -G4 - G5]
    ])

    B = np.array([
        [-IZ],
        [I2],
        [I1 - I2]
    ])

    X = np.linalg.solve(A, B)
    UA, UB, UC = [i[0] for i in X]

    UR4 = UB - UC
    IR4 = G4 * UR4

    print(f"{IZ=}")
    print(f"{G1=}")
    print(f"{G2=}")
    print(f"{G3=}")
    print(f"{G4=}")
    print(f"{G5=}")
    print(f"{UA=}")
    print(f"{UB=}")
    print(f"{UC=}")
    print(f"{UR4=}")
    print(f"{IR4=}")
    print(f"{X=}")

    A = np.array([
        [-G1 - G2 - G3, G2, 0],
        [G2, -G2 - G4, G4],
        [0, G4, -G4 - G5]
    ])

    B = np.array([
        [-IZ],
        [I2],
        [I1 - I2]
    ])
    print(f"{-G1 - G2 - G3=}")
    print(f"{-G2 - G4=}")
    print(f"{-G4 - G5=}")
    print(f"{-IZ=}")
    print(f"{I1 - I2=}")

third()