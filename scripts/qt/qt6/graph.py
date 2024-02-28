import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCharts import QChart
from PyQt6.QtCharts import QChartView
from PyQt6.QtCharts import QLineSeries
from PyQt6.QtCharts import QValueAxis

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример графика")
        self.setGeometry(100, 100, 600, 400)

        # Создание графика
        chart = QChart()
        chart.setTitle("Пример графика")

        # Создание и добавление графического представления
        chart_view = QChartView(chart)
        
        self.setCentralWidget(chart_view)

        x_values = [1, 2, 3, 4, 5]
        y_values = [2, 4, 8, 16, 32]

        series = QLineSeries()

        # Добавляем данные в серию
        for x, y in zip(x_values, y_values):
            series.append(x, y)

        chart.addSeries(series)

        target = 10
        series_line = QLineSeries()
        series_line.append(x_values[0], target)
        series_line.append(x_values[-1], target)

        chart.addSeries(series_line)

        # Настройка осей
        axis_x = QValueAxis()
        axis_y = QValueAxis()

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)
        series_line.attachAxis(axis_x)
        series_line.attachAxis(axis_y)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
