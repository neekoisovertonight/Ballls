import numpy as np  # для операций над векторами
import math as mt  # для математических операций
import matplotlib.pyplot as plt  # для построения графиков


# функция, осуществляющая наполнение массива углами от 0 до 360
def appendAngles(Ang):
    for i in range(360):
        Ang.append(i)


# функция, осуществляющая наполнение массива нулевыми значения для дальнейшей записи значений энергии шаров
def appenderNulls(E):
    for j in range(3):
        E1 = []
        for i in range(360):
            E1.append(0)
        E.append(E1)


# функция, осуществляющая построение графика зависимости энергии изначально покоящегося шара от угла удара
def plot(Angles, E):
    plt.figure()
    plt.plot(Angles, E[0], 'o-r', label="µ1 = 0.01", lw=1)
    plt.plot(Angles, E[1], 'o-b', label="µ2 = 0.05", lw=1)
    plt.plot(Angles, E[2], 'o-g', label="µ3 = 0.1", lw=1)
    plt.xlabel('Угол α (град)')
    plt.ylabel('Энергия шара Е (Дж)')
    plt.legend()
    plt.grid(True)
    plt.show()


# функция, осуществляющая вычисление столкновений шаров и подчёт их энергий

#receivingBallV0, restBallV0, receivingBallX, receivingBallY, dt, n, g, restBallX, restBallY, holeCoordinateX, holeCoordinateY, E, k, i, ballM, ballR, tableLengthX, widthTableY, holeR
def collusionsCalc(receivingBallV0, restBallV0, receivingBallX, receivingBallY, t, n1, g, restBallX, restBallY, holeCoordinateX, holeCoordinateY, E, coef, i, ballM, ballR, tableLengthX, widthTableY, R):
    # вспомогательные переменные для расчетов и рассмотрения всех возможных случаев
    angle1 = round(mt.radians(i), 5)
    angle2 = 0
    l = 0
    q = 0
    w = 0
    p = 0
    b = 0
    Vy0 = round(receivingBallV0 * mt.sin(angle1), 3)
    Vx0 = round(receivingBallV0 * mt.cos(angle1), 3)
    Vx2 = 0
    Vy2 = 0
    while (receivingBallV0 > 0) or (restBallV0 > 0):  # выполняется до остановки одного из шаров
        if receivingBallV0 > 0:
            if Vx0 != 0:
                receivingBallX = receivingBallX + Vx0 * t  # вычисление координаты Х шара, по которому бьют
            if Vy0 != 0:
                receivingBallY = receivingBallY + Vy0 * t  # вычисление координаты У шара, по которому бьют
            receivingBallV0 = receivingBallV0 - (n1 * g * t)
            if angle1 == 0 or angle1 == round(mt.radians(180), 5) or angle1 == round(mt.radians(270),
                                                                                     5) or angle1 == round(
                    mt.radians(90), 5):
                if angle1 == 0 or angle1 == round(mt.radians(180), 5):
                    Vy0 = 0
                    if angle1 == 0:
                        Vx0 = receivingBallV0
                    else:
                        Vx0 = -receivingBallV0
                else:
                    Vx0 = 0
                    if angle1 == round(mt.radians(90), 5):
                        Vy0 = receivingBallV0
                    else:
                        Vy0 = -receivingBallV0
            else:
                Vx0 = round(receivingBallV0 * mt.cos(angle1), 3)
                Vy0 = round(receivingBallV0 * mt.sin(angle1), 3)
            if receivingBallV0 < 0:
                receivingBallV0 = 0
                Vx0 = 0
                Vy0 = 0
        if restBallV0 > 0:
            if Vx2 != 0:
                restBallX = restBallX + Vx2 * t
            if Vy2 != 0:
                restBallY = restBallY + Vy2 * t
            restBallV0 = restBallV0 - (n1 * g * t)
            Vx2 = round(restBallV0 * mt.cos(angle2), 3)
            Vy2 = round(restBallV0 * mt.sin(angle2), 3)
            if restBallV0 < 0:
                restBallV0 = 0
                Vx2 = 0
                Vy2 = 0
        if mt.sqrt(mt.pow((receivingBallX - holeCoordinateX), 2) + mt.pow((receivingBallY - holeCoordinateY), 2)) <= R:
            receivingBallV0 = 0
            receivingBallX = holeCoordinateX
            receivingBallY = holeCoordinateY
        if mt.sqrt(mt.pow((restBallX - holeCoordinateX), 2) + mt.pow((restBallY - holeCoordinateY), 2)) <= R:
            E[coef][i] = ballM * restBallV0 * restBallV0 / 2.0
            restBallV0 = 0
            receivingBallV0 = 0
            continue  # так как энергия вычислена, можно завершать выполнение цикла while
        if ((receivingBallX + ballR) >= tableLengthX or (receivingBallX - ballR) <= 0) and w == 0:
            Vx0 = -Vx0
            angle1 = round(mt.radians(180) - angle1, 5)
            w = 1
        else:
            w = 0
        if ((receivingBallY + ballR) >= widthTableY or (receivingBallY - ballR) <= 0) and p == 0:
            Vy0 = -Vy0
            angle1 = round(angle1 - mt.radians(180), 5)
            p = 1
        else:
            p = 0
        if ((restBallX + ballR) >= tableLengthX or (restBallX - ballR) <= 0) and q == 0:
            Vx2 = -Vx2
            angle2 = round(mt.radians(180) - angle2, 5)
            q = 1
        else:
            q = 0
        if ((restBallY + ballR) >= widthTableY or (restBallY - ballR) <= 0) and b == 0:
            Vy2 = -Vy2
            angle2 = round(angle2 - mt.radians(180), 5)
            b = 1
        else:
            b = 0
        if mt.sqrt(mt.pow((receivingBallX - restBallX), 2) + mt.pow((receivingBallY - restBallY), 2)) <= (2 * ballR) and l == 0:
            en = np.array([round((restBallX - receivingBallX) / (2 * ballR), 3), round((restBallY - receivingBallY) / (2 * ballR), 3)])
            et = np.array([round((receivingBallY - restBallY) / (2 * ballR), 3), round((restBallX - receivingBallX) / (2 * ballR), 3)])
            Vvect = np.array([Vx0, Vy0])
            V2vect = np.array([Vx2, Vy2])
            Vvect = (round(np.dot(V2vect, en), 3) * en) + (round(np.dot(Vvect, et), 3) * et)
            V2vect = (round(np.dot(np.array([Vx0, Vy0]), en), 3) * en) + (round(np.dot(V2vect, et), 3) * et)
            Vx0 = round(Vvect[0], 3)
            Vy0 = round(Vvect[1], 3)
            Vx2 = round(V2vect[0], 3)
            Vy2 = round(V2vect[1], 3)
            receivingBallV0 = round(np.linalg.norm(Vvect), 3)
            restBallV0 = round(np.linalg.norm(V2vect), 3)
            if receivingBallV0 != 0:
                angle1 = round(mt.acos(round((Vx0 / receivingBallV0), 3)), 5)
            else:
                Vx0 = 0
                Vy0 = 0
                angle1 = 0
            if restBallV0 != 0:
                angle2 = round(mt.acos(round((Vx2 / restBallV0), 3)), 5)
            else:
                Vx2 = 0
                Vy2 = 0
                angle2 = 0
            l = 1
        else:
            l = 0
