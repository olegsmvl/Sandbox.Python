import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Window')
        self.setGeometry(100, 100, 300, 200)
        
        self.button = QPushButton('Нажми меня', self)
        self.button.setGeometry(100, 100, 100, 50)

        # Привязываем функцию к событию "clicked" (нажатие на кнопку)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        # Создаем диалоговое окно с сообщением
        QMessageBox.information(self, 'Сообщение', 'Кнопка была нажата!')

if __name__ == '__main__':
    app = QApplication([])
    window = SimpleWindow()

    window.show()
    app.exec()