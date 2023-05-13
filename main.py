import methods

tableLengthX = 2.0
widthTableY = 2.0
holeCoordinateX = 1.7 # координата Х лузы
holeCoordinateY = 0.3 # координата У лузы
holeR = 0.2 # радиус лузы
ballR = 0.05 # радиус шариков
ballM = 0.3 # масса шариков
frictionCoefficient1 = 0.0001 # коэффициент трения 1
frictionCoefficient2 = 0.05 # коэффициент трения 2
frictionCoefficient3 = 0.1 # коэффициент трения 3

E = []
Angles = []
methods.appenderNulls(E) # функция, осуществляющая наполнение массива нулевыми значения для дальнейшей записи значений энергии шаров
methods.appendAngles(Angles) # функция, осуществляющая наполнение массива углами от 0 до 360
n = 0
g = 9.8
dt = 0.1
for coef in range(3):
    if coef == 0:
        n = frictionCoefficient1
    if coef == 1:
        n = frictionCoefficient2
    if coef == 2:
        n = frictionCoefficient3
    for i in range(360):
        receivingBallX = 0.2 # координата Х шара, по которому бьют
        receivingBallY = 0.5 # координата У шара, по которому бьют
        restBallX = 1 # координата Х шара, изначально покоящегося
        restBallY = 0.3 # координата У шара, изначально покоящегося
        receivingBallV0 = 2 # начальная скорость шара, по которому бьют
        restBallV0 = 0 # начальная скорость покоящегося шара

        methods.collusionsCalc(receivingBallV0, restBallV0, receivingBallX, receivingBallY, dt, n, g, restBallX, restBallY, holeCoordinateX, holeCoordinateY, E, coef, i, ballM, ballR, tableLengthX, widthTableY, holeR)
methods.plot(Angles, E)
