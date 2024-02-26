from PySide6.QtCore import QObject, Signal, Property, QTimer, Slot
from can_provider import CanController

class Model(QObject):
    secondsChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._seconds_counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)
        self.timer.start(1000)
        self.can = CanController()

    @Property(int, notify=secondsChanged)
    def secondsCounter(self):
        return self._seconds_counter

    def update_counter(self):
        self._seconds_counter += 1
        self.secondsChanged.emit(self._seconds_counter)

    @Slot()
    def incrementCounter(self):
        self._seconds_counter += 1
        self.secondsChanged.emit(self._seconds_counter)

    @Slot()
    def connect(self):
        self.can.connect()

