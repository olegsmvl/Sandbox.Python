import sys
from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class YourModel(QObject):
    somePropertyChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._some_property = 0

    @Property(int, notify=somePropertyChanged)
    def someProperty(self):
        return self._some_property

    @someProperty.setter
    def someProperty(self, value):
        if self._some_property != value:
            self._some_property = value
            self.somePropertyChanged.emit(self._some_property)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    your_model = YourModel()
    engine.rootContext().setContextProperty("yourModel", your_model)

    engine.load("qml/test.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
