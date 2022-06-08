# -*- coding: utf-8 -*-
# __author__ = 'Kratos'
# Form implementation generated from reading ui file 'Camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import sys
sys.setrecursionlimit(1000000000)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from matplotlib import pyplot as plt
import math
import numpy as np


class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.resize(525, 350)


        self.label1 = QtWidgets.QLabel(Camera)
        self.label1.setGeometry(QtCore.QRect(70, 20, 131, 24))
        self.label1.setObjectName("alpha")
        self.label2 = QtWidgets.QLabel(Camera)
        self.label2.setGeometry(QtCore.QRect(70, 70, 131, 24))
        self.label2.setObjectName("beta")
        self.label3 = QtWidgets.QLabel(Camera)
        self.label3.setGeometry(QtCore.QRect(70, 120, 141, 24))
        self.label3.setObjectName("distance")
        self.label4 = QtWidgets.QLabel(Camera)
        self.label4.setGeometry(QtCore.QRect(70, 170, 121, 24))
        self.label4.setObjectName("h_angle")
        self.label5 = QtWidgets.QLabel(Camera)
        self.label5.setGeometry(QtCore.QRect(70, 220, 121, 24))
        self.label5.setObjectName("v_angle")
        self.label6 = QtWidgets.QLabel(Camera)
        self.label6.setGeometry(QtCore.QRect(430, 330, 100, 20))
        self.label6.setObjectName("author")
        self.label7 = QtWidgets.QLabel(Camera)
        self.label7.setGeometry(QtCore.QRect(70, 270, 141, 24))
        self.label7.setObjectName("average_height")

        self.displayAlpha = QtWidgets.QLineEdit(Camera)
        self.displayAlpha.setGeometry(QtCore.QRect(250, 20, 91, 24))
        self.displayAlpha.setObjectName("alpha")
        self.displayAlpha.setText("90.00")
        self.displayAlpha.setReadOnly(True)
        self.displayBeta = QtWidgets.QLineEdit(Camera)
        self.displayBeta.setGeometry(QtCore.QRect(250, 70, 91, 24))
        self.displayBeta.setObjectName("beta")
        self.displayBeta.setText("90.00")
        self.displayBeta.setReadOnly(True)
        self.displayDistance = QtWidgets.QLineEdit(Camera)
        self.displayDistance.setGeometry(QtCore.QRect(250, 120, 91, 24))
        self.displayDistance.setObjectName("distance")
        self.displayDistance.setText("2.00")
        self.displayDistance.setReadOnly(True)
        self.displayH_angle = QtWidgets.QLineEdit(Camera)
        self.displayH_angle.setGeometry(QtCore.QRect(250, 170, 91, 24))
        self.displayH_angle.setObjectName("h_angle")
        self.displayH_angle.setText("0.00")
        self.displayH_angle.setReadOnly(True)
        self.displayV_angle = QtWidgets.QLineEdit(Camera)
        self.displayV_angle.setGeometry(QtCore.QRect(250, 220, 91, 24))
        self.displayV_angle.setObjectName("v_angle")
        self.displayV_angle.setText("0.00")
        self.displayV_angle.setReadOnly(True)
        self.displayHeight = QtWidgets.QLineEdit(Camera)
        self.displayHeight.setGeometry(QtCore.QRect(250, 270, 91, 24))
        self.displayHeight.setObjectName("average_height")
        self.displayHeight.setText("1.60")
        self.displayHeight.setReadOnly(True)


        self.pushAlpha = QtWidgets.QPushButton(Camera)
        self.pushAlpha.setGeometry(QtCore.QRect(380, 20, 75, 24))
        self.pushAlpha.setObjectName("输入alpha")
        self.pushAlpha.setText("输入")
        self.pushBeta = QtWidgets.QPushButton(Camera)
        self.pushBeta.setGeometry(QtCore.QRect(380, 70, 75, 24))
        self.pushBeta.setObjectName("输入beta")
        self.pushBeta.setText("输入")
        self.pushDistance = QtWidgets.QPushButton(Camera)
        self.pushDistance.setGeometry(QtCore.QRect(380, 120, 75, 24))
        self.pushDistance.setObjectName("输入distance")
        self.pushDistance.setText("输入")
        self.pushH_angle = QtWidgets.QPushButton(Camera)
        self.pushH_angle.setGeometry(QtCore.QRect(380, 170, 75, 24))
        self.pushH_angle.setObjectName("输入h_angle")
        self.pushH_angle.setText("输入")
        self.pushV_angle = QtWidgets.QPushButton(Camera)
        self.pushV_angle.setGeometry(QtCore.QRect(380, 220, 75, 24))
        self.pushV_angle.setObjectName("输入v_angle")
        self.pushV_angle.setText("输入")
        self.pushButton6 = QtWidgets.QPushButton(Camera)
        self.pushButton6.setGeometry(QtCore.QRect(300, 320, 75, 24))
        self.pushButton6.setObjectName("ok")
        self.pushButton7 = QtWidgets.QPushButton(Camera)
        self.pushButton7.setGeometry(QtCore.QRect(150, 320, 75, 24))
        self.pushButton7.setObjectName("cancel")
        self.pushHeight = QtWidgets.QPushButton(Camera)
        self.pushHeight.setGeometry(QtCore.QRect(380, 270, 75, 24))
        self.pushHeight.setObjectName("输入Height")
        self.pushHeight.setText("输入")


        self.alphaInput = QtWidgets.QLabel("0.00")
        self.alphaInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.betaInput = QtWidgets.QLabel("0.00")
        self.betaInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.distanceInput = QtWidgets.QLabel("2.00")
        self.distanceInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.h_angleInput = QtWidgets.QLabel("0.00")
        self.h_angleInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.v_angleInput = QtWidgets.QLabel("0.00")
        self.v_angleInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.heightInput = QtWidgets.QLabel("1.60")
        self.heightInput.setFrameStyle(QFrame.Panel | QFrame.Sunken)


        self.retranslateUi(Camera)
        self.pushAlpha.clicked.connect(self.getAlpha)
        self.pushBeta.clicked.connect(self.getBeta)
        self.pushDistance.clicked.connect(self.getDistance)
        self.pushH_angle.clicked.connect(self.getH_angle)
        self.pushV_angle.clicked.connect(self.getV_angle)
        self.pushButton6.clicked.connect(self.paint)
        self.pushButton7.clicked.connect(self.close)   #or Camera.close
        self.pushHeight.clicked.connect(self.getHeight)

        QtCore.QMetaObject.connectSlotsByName(Camera)


    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "Form"))
        self.label1.setText(_translate("Camera", "相机的水平视角α(°)："))
        self.label2.setText(_translate("Camera", "相机的垂直视角β(°)："))
        self.label3.setText(_translate("Camera", "相机中心到平面距离d(m)："))
        self.label4.setText(_translate("Camera", "水平偏转角θ1(°)："))
        self.label5.setText(_translate("Camera", "垂直偏转角θ2(°)："))
        self.label7.setText(_translate("Camera", "观测对象的平均高度h(m)："))
        self.label6.setText(_translate("Camera", "Author: Kratos"))
        self.pushButton6.setText(_translate("Camera", "绘制"))
        self.pushButton7.setText(_translate("Camera", "退出"))


    def getAlpha(self):
        alpha, ok = QInputDialog.getDouble(self, "Alpha", "输入相机视角范围α(0 < α < 180)：", float(self.alphaInput.text()), 0.01, 180.00, 2)
        if ok:
            self.displayAlpha.setText(str(alpha))


    def getBeta(self):
        beta, ok = QInputDialog.getDouble(self, "Beta", "输入相机视角范围β(0 < β < 180)：", float(self.betaInput.text()), 0.01, 180.00, 2)
        if ok:
            self.displayBeta.setText(str(beta))


    def getDistance(self):
        distance, ok = QInputDialog.getDouble(self, "Distance", "输入相机中心到平面距离d(2 ≤ d ≤ 7)：", float(self.distanceInput.text()), 2.00, 7.00, 2)
        if ok:
            self.displayDistance.setText(str(distance))

    def getHeight(self):
        height, ok = QInputDialog.getDouble(self, "Height", "输入观测对象的平均高度h(1.3 ≤ d ≤ 2)：", float(self.heightInput.text()), 1.3, 2, 2)
        if ok:
            self.displayHeight.setText(str(height))


    def getH_angle(self):
        h_angle, ok = QInputDialog.getDouble(self, "Horizontal Deflection Angle", "输入水平偏转角(-40 ≤ d ≤ 40)：", float(self.h_angleInput.text()), -40.00, 40.00, 2)
        if ok:
            self.displayH_angle.setText(str(h_angle))


    def getV_angle(self):
        v_angle, ok = QInputDialog.getDouble(self, "Verticle Deflection Angle", "输入水平偏转角(-30 ≤ d ≤ 30)：", float(self.v_angleInput.text()), -30.00, 30.00, 2)
        if ok:
            self.displayV_angle.setText(str(v_angle))


    def paint(self):
        alpha = float(self.displayAlpha.text())
        beta = float(self.displayBeta.text())
        h = float(self.displayDistance.text())
        average_height = float(self.displayHeight.text())
        theta1 = float(self.displayH_angle.text())
        theta2 = float(self.displayV_angle.text())

        # average_height = 1.6
        h_human = h - average_height

        alpha = math.radians(alpha)
        beta = math.radians(beta)
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)

        # 计算各个点坐标（单位米）
        a = h * math.tan(alpha/2)  # 水平方向一半视角
        b = h * math.tan(beta/2)  # 垂直方向一半视角

        Rx = np.array([[1, 0, 0], [0, math.cos(theta2), math.sin(theta2)], [0, -math.sin(theta2), math.cos(theta2)]])
        theta_pi = math.acos(math.sqrt(pow(math.tan(theta2), 2) + 1) / math.sqrt(pow(math.tan(theta1), 2) + pow(math.tan(theta2), 2) + 1))
        Ry = np.array([[math.cos(theta_pi), 0, math.sin(theta_pi)], [0, 1, 0], [-math.sin(theta_pi), 0, math.cos(theta_pi)]])
        R = Ry @ Rx

        A = np.array([h * math.tan(alpha/2), h * math.tan(beta/2), h])
        B = np.array([-h * math.tan(alpha/2), h * math.tan(beta/2), h])
        C = np.array([-h * math.tan(alpha/2), -h * math.tan(beta/2), h])
        D = np.array([h * math.tan(alpha/2), -h * math.tan(beta/2), h])

        A_pi = R @ A
        B_pi = R @ B
        C_pi = R @ C
        D_pi = R @ D

        A_focus = np.array([A_pi[0] * h / A_pi[2], A_pi[1] * h / A_pi[2]])
        B_focus = np.array([B_pi[0] * h / B_pi[2], B_pi[1] * h / B_pi[2]])
        C_focus = np.array([C_pi[0] * h / C_pi[2], C_pi[1] * h / C_pi[2]])
        D_focus = np.array([D_pi[0] * h / D_pi[2], D_pi[1] * h / D_pi[2]])
        # print(A_focus[0], A_focus[1])

        # 计算各个点坐标（单位英尺）
        a_human = h_human * math.tan(alpha/2)  # 水平方向一半视角
        b_human = h_human * math.tan(beta/2)  # 垂直方向一半视角

        A_human = np.array([h_human * math.tan(alpha/2), h_human * math.tan(beta/2), h_human])
        B_human = np.array([-h_human * math.tan(alpha/2), h_human * math.tan(beta/2), h_human])
        C_human = np.array([-h_human * math.tan(alpha/2), -h_human * math.tan(beta/2), h_human])
        D_human = np.array([h_human * math.tan(alpha/2), -h_human * math.tan(beta/2), h_human])

        A_pi_human = R @ A_human
        B_pi_human = R @ B_human
        C_pi_human = R @ C_human
        D_pi_human = R @ D_human

        A_focus_human = np.array([A_pi_human[0] * h_human / A_pi_human[2], A_pi_human[1] * h_human / A_pi_human[2]])
        B_focus_human = np.array([B_pi_human[0] * h_human / B_pi_human[2], B_pi_human[1] * h_human / B_pi_human[2]])
        C_focus_human = np.array([C_pi_human[0] * h_human / C_pi_human[2], C_pi_human[1] * h_human / C_pi_human[2]])
        D_focus_human = np.array([D_pi_human[0] * h_human / D_pi_human[2], D_pi_human[1] * h_human / D_pi_human[2]])

        x1 = A_focus[0]
        y1 = A_focus[1]
        x2 = B_focus[0]
        y2 = B_focus[1]
        x3 = D_focus[0]
        y3 = D_focus[1]
        x4 = C_focus[0]
        y4 = C_focus[1]
        x = [x1,x2,x4,x3]
        y = [y1,y2,y4,y3]

        x1_human = A_focus_human[0]
        y1_human = A_focus_human[1]
        x2_human = B_focus_human[0]
        y2_human = B_focus_human[1]
        x3_human = D_focus_human[0]
        y3_human = D_focus_human[1]
        x4_human = C_focus_human[0]
        y4_human = C_focus_human[1]
        x_human = [x1_human,x2_human,x4_human,x3_human]
        y_human = [y1_human,y2_human,y4_human,y3_human]

        # 单位为米
        plt.subplot(211)
        plt.grid(True)
        plt.plot(x,y, color = 'b')
        plt.plot([x1,x3],[y1,y3], color = 'b')
        plt.scatter(x, y, color = 'b')
        plt.scatter(0, 0, color = 'g')

        plt.plot(x_human,y_human, color = 'b')
        plt.plot([x1_human,x3_human],[y1_human,y3_human], color = 'b')
        plt.scatter(x_human, y_human, color = 'b')

        plt.annotate(r'$(%.2f,%.2f)$' % (x1,y1), xy=(x1, y1), xycoords='data', xytext=(x1, y1), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x2,y2), xy=(x2, y2), xycoords='data', xytext=(x2, y2), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x3,y3), xy=(x3, y3), xycoords='data', xytext=(x3, y3), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x4,y4), xy=(x4, y4), xycoords='data', xytext=(x4, y4), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x1_human,y1_human), xy=(x1_human, y1_human), xycoords='data', xytext=(x1_human, y1_human), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x2_human,y2_human), xy=(x2_human, y2_human), xycoords='data', xytext=(x2_human, y2_human), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x3_human,y3_human), xy=(x3_human, y3_human), xycoords='data', xytext=(x3_human, y3_human), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x4_human,y4_human), xy=(x4_human, y4_human), xycoords='data', xytext=(x4_human, y4_human), textcoords='offset points', fontsize=10, color = 'r')
        plt.title("Coverage Area - Meters")

        # 单位换算
        x1_inches = 39.37 * x1
        y1_inches = 39.37 * y1
        x2_inches = 39.37 * x2
        y2_inches = 39.37 * y2
        x3_inches = 39.37 * x3
        y3_inches = 39.37 * y3
        x4_inches = 39.37 * x4
        y4_inches = 39.37 * y4
        x1_human_inches = 39.37 * x1_human
        y1_human_inches = 39.37 * y1_human
        x2_human_inches = 39.37 * x2_human
        y2_human_inches = 39.37 * y2_human
        x3_human_inches = 39.37 * x3_human
        y3_human_inches = 39.37 * y3_human
        x4_human_inches = 39.37 * x4_human
        y4_human_inches = 39.37 * y4_human

        # 单位为英尺
        plt.subplot(212)
        plt.grid(True)
        plt.plot([x1_inches,x2_inches],[y1_inches,y2_inches], color = 'b')
        plt.plot([x1_inches,x3_inches],[y1_inches,y3_inches], color = 'b')
        plt.plot([x2_inches,x4_inches],[y2_inches,y4_inches], color = 'b')
        plt.plot([x3_inches,x4_inches],[y3_inches,y4_inches], color = 'b')
        plt.scatter(x1_inches, y1_inches, color = 'b')
        plt.scatter(x2_inches, y2_inches, color = 'b')
        plt.scatter(x3_inches, y3_inches, color = 'b')
        plt.scatter(x4_inches, y4_inches, color = 'b')

        plt.plot([x1_human_inches,x2_human_inches],[y1_human_inches,y2_human_inches], color = 'b')
        plt.plot([x1_human_inches,x3_human_inches],[y1_human_inches,y3_human_inches], color = 'b')
        plt.plot([x2_human_inches,x4_human_inches],[y2_human_inches,y4_human_inches], color = 'b')
        plt.plot([x3_human_inches,x4_human_inches],[y3_human_inches,y4_human_inches], color = 'b')
        plt.scatter(x1_human_inches, y1_human_inches, color = 'b')
        plt.scatter(x2_human_inches, y2_human_inches, color = 'b')
        plt.scatter(x3_human_inches, y3_human_inches, color = 'b')
        plt.scatter(x4_human_inches, y4_human_inches, color = 'b')

        plt.scatter(0, 0, color = 'g')

        plt.annotate(r'$(%.2f,%.2f)$' % (x1_inches,y1_inches), xy=(x1_inches, y1_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x2_inches,y2_inches), xy=(x2_inches, y2_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x3_inches,y3_inches), xy=(x3_inches, y3_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x4_inches,y4_inches), xy=(x4_inches, y4_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
		
        plt.annotate(r'$(%.2f,%.2f)$' % (x1_human_inches,y1_human_inches), xy=(x1_human_inches, y1_human_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x2_human_inches,y2_human_inches), xy=(x2_human_inches, y2_human_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x3_human_inches,y3_human_inches), xy=(x3_human_inches, y3_human_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')
        plt.annotate(r'$(%.2f,%.2f)$' % (x4_human_inches,y4_human_inches), xy=(x4_human_inches, y4_human_inches), xycoords='data', xytext=(0, 0), textcoords='offset points', fontsize=10, color = 'r')

        plt.title("Coverage Area - Inches")

        plt.show()


class mwindow(QWidget, Ui_Camera):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)
        self.Icon()


    #图标
    def Icon(self):
        self.setWindowIcon(QIcon('C:/Users/yfc/Desktop/Camera.ico'))


if __name__=='__main__':
    app = QApplication(sys.argv)
    myWin = mwindow()
    myWin.setWindowTitle("Camera Test")
    myWin.show()
    sys.exit(app.exec())
