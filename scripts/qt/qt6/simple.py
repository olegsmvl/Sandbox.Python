from PyQt6.QtWidgets import QApplication, QWidget

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Window')
        self.setGeometry(100, 100, 300, 200)

        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = SimpleWindow()
    app.exec()