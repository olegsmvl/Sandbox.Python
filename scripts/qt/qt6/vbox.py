import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QCheckBox,
)


class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Window")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Нажми меня", self)
        # self.button.setFixedHeight(20)

        self.button_2 = QPushButton("Нажми меня 2", self)
        # self.button_2.setFixedHeight(20)

        # Привязываем функцию к событию "clicked" (нажатие на кнопку)
        self.button.clicked.connect(self.show_message)

        self.check = QCheckBox("chk")
        self.check.checkState = True

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button_2)
        layout.addWidget(self.check)

        self.setLayout(layout)

    def show_message(self):
        # Создаем диалоговое окно с сообщением
        QMessageBox.information(self, "Сообщение", "Кнопка была нажата!")


if __name__ == "__main__":
    app = QApplication([])
    window = SimpleWindow()

    window.show()
    app.exec()
