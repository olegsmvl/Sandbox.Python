from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window's properties
        self.setWindowTitle('PyQt6 Combo Box Example')
        self.setGeometry(100, 100, 280, 100)

        # Create a combo box and add some items
        self.combo_box = QComboBox()
        self.combo_box.addItems(['Option 1', 'Option 2', 'Option 3', 'Option 4'])

        # Create a label to display the selected option
        self.label = QLabel('Select an option')
        self.label.setFixedHeight(20)

        # Connect the combo box's signal to the slot
        self.combo_box.currentTextChanged.connect(self.update_label)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)

        # Create a central widget, set its layout, and set it to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_label(self, text):
        self.label.setText(f'Selected: {text}')

# Create an instance of QApplication
app = QApplication([])

# Create an instance of the main window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec()
