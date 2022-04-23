from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import matplotlib.pyplot as plt
import socket
import time

server_name = '127.0.0.1'
server_port = 12001

# create a socket object
t = [0]
p = [0]

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


        self.x = list(range(100))  # 100 time points
        self.y = list(range(100))  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        start = time.time()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_name, server_port))
        sentence = "Normal Client"
        client.send(sentence.encode())
        modifiedSentence = client.recvfrom(2048)
        print(modifiedSentence[0].decode())
        client.close()
        end = time.time()
        print("Eclipsed time: %f" % (end - start))







        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(end - start)  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())