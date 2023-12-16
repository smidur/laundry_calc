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
        ils_label = QLabel("ILS: ")
        self.ils_line_edit = QLineEdit()
        usd_label = QLabel("USD: ")
        self.usd_line_edit = QLineEdit()

        # button
        calculate_button = QPushButton("CALCULATE")
        calculate_button.clicked.connect(self.calculate)
        calculate_button.pressed.connect(self.calculate)

        # output
        self.vat_label = QLabel()
        self.no_vat_label = QLabel()

        # add widget to grid
        grid.addWidget(combobox, 0, 0, 1, 2)

        grid.addWidget(ils_label, 1, 0)
        grid.addWidget(self.ils_line_edit, 1, 1)
        grid.addWidget(self.vat_label, 2, 0)
        grid.addWidget(self.no_vat_label, 2, 1)
        # else:
        #     grid.addWidget(usd_label, 1, 0)
        #     grid.addWidget(self.usd_line_edit, 1, 1)
        #     grid.addWidget(self.vat_label, 2, 0)
        #     grid.addWidget(self.no_vat_label, 2, 1)

        grid.addWidget(calculate_button, 3, 0, 1, 2)
        # else:

        self.setLayout(grid)

    def calculate(self):
        ils = float(self.ils_line_edit.text())
        no_vat = round(ils / 3.5 / 1.17, 2)
        vat = ils / 3.5
        self.no_vat_label.setText(str(no_vat))
        self.vat_label.setText(str(vat))


app = QApplication(sys.argv)
calc = LaundryCalculator()
calc.show()
sys.exit(app.exec())
