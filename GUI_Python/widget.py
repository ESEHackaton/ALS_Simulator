__author__ = "Thomas Randwijk & Lucas Bolwidt"
__copyright__ = "Open Source"
__license__ = "Public Domain"
__version__ = "1.0"

'''
Graphical representation of ECG and HRV. Based on Qt6, generation of ECG and RSP values

Features:
    - Generates a complete ECG for child, with 1 fast and 1 slow BPM.
    - Uses fast algorithm for usage on Raspberry PI.

Recommended Changes:
    - Add Sensordata
    - ECG smooth transition
'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
import numpy as np
import pyqtgraph as pg
import neurokit2 as nk              #neurokit2 library for creating ECG & RSP signal

class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.ecg_rate = 50  # Default heart rate
        self.create_ecg_signal()

        #Initializes Plot
        self.plot_widget_sin = pg.PlotWidget()
        self.plot_widget_cos = pg.PlotWidget()

        #Ceates box for formatting
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.plot_widget_sin)
        self.layout().addWidget(self.plot_widget_cos)

        #Fill lines for first time
        self.x_sin = np.linspace(0, 10, len(self.ecg_part))
        self.x_cos = np.linspace(0, 20, len(self.rsp15_part))
        self.y_sin = self.ecg_part
        self.y_cos = self.rsp15_part

        #Setup lines for upper & bottom plot
        self.curve_sin = self.plot_widget_sin.plot(self.x_sin, self.y_sin, pen='b', name='Sinus')
        self.curve_cos = self.plot_widget_cos.plot(self.x_cos, self.y_cos, pen='r', name='Cosinus')

        # Set titles for the plot widgets
        self.plot_widget_sin.setTitle("ECG")
        self.plot_widget_cos.setTitle("Respiration")

        # Add button to switch between ECG signals
        self.button_switch_ecg = QPushButton("Switch ECG")
        self.button_switch_ecg.clicked.connect(self.switch_ecg_signal)
        self.layout().addWidget(self.button_switch_ecg)

        # Set up a QTimer to update the x-axis at regular intervals
        self.timer = pg.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # Update every 100 milliseconds


    def create_ecg_signal(self):
        # Generate ECG & RSP using NeuroKit library
        self.ecg_part = nk.ecg_simulate(duration=10, sampling_rate=500, noise=0.1, heart_rate=self.ecg_rate).ravel()
        self.rsp15_part = nk.rsp_simulate(duration=20, sampling_rate=800, noise=0.005, respiratory_rate=15, method="breathmetrics").ravel()

    def switch_ecg_signal(self):
        # Toggle between ECG signals with heart rates of 50 and 100
        self.ecg_rate = 100 if self.ecg_rate == 50 else 50
        self.create_ecg_signal()

    def update_plot(self):
        # Increment the x-axis values to simulate advancing time
        self.x_sin += 0.1
        self.x_cos += 0.1

        # Update the plot with the constant sinusoidal and cosinusoidal data
        self.curve_sin.setData(self.x_sin, self.ecg_part)
        self.curve_cos.setData(self.x_cos, self.rsp15_part)

        self.ecg_part = np.roll(self.ecg_part, -50)
        self.rsp15_part = np.roll(self.rsp15_part, -50)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.graph_widget = GraphWidget()
        layout.addWidget(self.graph_widget)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
