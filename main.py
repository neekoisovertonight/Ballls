import methods


length_table_X = 2.0
width_table_Y = 2.0
holeCoordinateX = 1.0 # координата Х лузы
holeCoordinateY = 1.0 # координата У лузы
holeR = 0.2 # радиус лузы
ballR = 0.05 # радиус шариков
ballM = 0.3 # масса шариков
frictionCoefficient1 = 0.01 # коэффициент трения 1
frictionCoefficient2 = 0.05 # коэффициент трения 2
frictionCoefficient3 = 0.1 # коэффициент трения 3

energy = []
for i in range(3):
    cur_energy = [0]*360
    energy.append(cur_energy)
# print(energy)
angles = []
for k in range(360):
    angles.append(k)
# print(angles)

n = 0
g = 9.81
dt = 0.1
for coef in range(3):
    if coef == 0:
        n = frictionCoefficient1
    if coef == 1:
        n = frictionCoefficient2
    if coef == 2:
        n = frictionCoefficient3
    for l in range(360):
        receivingBallX = 1.9 # координата Х шара, по которому бьют
        receivingBallY = 0.1 # координата У шара, по которому бьют
        restBallX = 1.9 # координата Х шара, изначально покоящегося
        restBallY = 1.8 # координата У шара, изначально покоящегося
        receivingBallV0 = 2 # начальная скорость шара, по которому бьют
        restBallV0 = 0 # начальная скорость покоящегося шара

        methods.collusionsCalc(receivingBallV0, restBallV0, receivingBallX, receivingBallY, dt, n, g, restBallX, restBallY, holeCoordinateX, holeCoordinateY, energy, coef, l, ballM, ballR, length_table_X, width_table_Y, holeR)
methods.plot(angles, energy)
