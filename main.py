from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QComboBox)
import sys


class LaundryCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Calculator")
        grid = QGridLayout()

        # create widgets
        combobox_options = ["from ILS", "from USD"]
        combobox = QComboBox()
        combobox.addItems(combobox_options)
        amount_label = QLabel("Amount: ")
        self.amount_line_edit = QLineEdit()
        vat_label = QLabel("With VAT: ")
        no_vat_label = QLabel("Without VAT: ")

        # button
        calculate_button = QPushButton("CALCULATE")
        calculate_button.clicked.connect(self.calculate)
        calculate_button.pressed.connect(self.calculate)

        # output
        self.vat_label_result = QLabel()
        self.no_vat_label_result = QLabel()

        # add widget to grid
        grid.addWidget(combobox, 1, 0, 1, 2)

        grid.addWidget(amount_label, 2, 0)
        grid.addWidget(self.amount_line_edit, 2, 1)
        grid.addWidget(calculate_button, 3, 0, 1, 2)
        grid.addWidget(vat_label, 4, 0)
        grid.addWidget(no_vat_label, 5, 0)
        grid.addWidget(self.vat_label_result, 4, 1)
        grid.addWidget(self.no_vat_label_result, 5, 1)

        with open("style.qss", "r") as f:
            style = f.read()
        self.setStyleSheet(style)
        self.setLayout(grid)

    def calculate(self):
        amount = float(self.amount_line_edit.text())
        no_vat = round(amount / 3.5 / 1.17, 2)
        vat = amount / 3.5
        self.no_vat_label_result.setText(str(no_vat))
        self.vat_label_result.setText(str(vat))


app = QApplication(sys.argv)
calc = LaundryCalculator()
calc.show()
sys.exit(app.exec())
