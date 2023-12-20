from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QComboBox, QSpinBox,
                             QDoubleSpinBox)
from PyQt6.QtCore import Qt
import sys


class LaundryCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Calculator")
        self.setMinimumWidth(400)
        self.setMinimumHeight(270)
        grid = QGridLayout()

        # create and add widgets
        rate_label = QLabel("Rate: ")
        self.rate_dbl_spinbox = QDoubleSpinBox()
        self.rate_dbl_spinbox.setRange(0.0, 10.0)
        self.rate_dbl_spinbox.setSingleStep(0.01)
        self.rate_dbl_spinbox.setValue(3.7)
        grid.addWidget(rate_label, 0, 0)
        grid.addWidget(self.rate_dbl_spinbox, 0, 1)

        vat_percent_label = QLabel("VAT: ")
        self.vat_percent_spinbox = QSpinBox()
        self.vat_percent_spinbox.setRange(0, 200)
        self.vat_percent_spinbox.setSingleStep(1)
        self.vat_percent_spinbox.setSuffix("%")
        self.vat_percent_spinbox.setValue(17)
        grid.addWidget(vat_percent_label, 0, 2)
        grid.addWidget(self.vat_percent_spinbox, 0, 3)

        amount_label = QLabel("Amount: ")
        self.amount_line_edit = QLineEdit()
        self.amount_line_edit.setPlaceholderText("479")
        grid.addWidget(amount_label, 1, 0)
        grid.addWidget(self.amount_line_edit, 1, 1)

        currency_options = ["ILS", "USD"]
        currency_combobox = QComboBox()
        currency_combobox.addItems(currency_options)
        grid.addWidget(currency_combobox, 1, 2, 1, 2)

        calculate_button = QPushButton("CALCULATE")
        calculate_button.clicked.connect(self.calculate)
        calculate_button.pressed.connect(self.calculate)
        grid.addWidget(calculate_button, 2, 1)

        self.vat_label = QLabel("With VAT: ")
        self.vat_label.setVisible(False)
        self.vat_label_result = QLabel()
        self.vat_label_result.setVisible(False)
        grid.addWidget(self.vat_label, 3, 0)
        grid.addWidget(self.vat_label_result, 3, 1)

        self.copy_vat_button = QPushButton("Copy")
        self.copy_vat_button.clicked.connect(self.copy_vat)
        self.copy_vat_button.pressed.connect(self.copy_vat)
        self.copy_vat_button.setVisible(False)
        grid.addWidget(self.copy_vat_button, 3, 2)

        self.copy_no_vat_button = QPushButton("Copy")
        self.copy_no_vat_button.clicked.connect(self.copy_no_vat)
        self.copy_no_vat_button.pressed.connect(self.copy_no_vat)
        self.copy_no_vat_button.setVisible(False)
        grid.addWidget(self.copy_no_vat_button, 3, 2)

        self.no_vat_label = QLabel("Without VAT: ")
        self.no_vat_label.setVisible(False)
        self.no_vat_label_result = QLabel()
        self.no_vat_label_result.setVisible(False)
        grid.addWidget(self.no_vat_label, 4, 0)
        grid.addWidget(self.no_vat_label_result, 4, 1)

        with open("style.qss", "r") as f:
            style = f.read()
        self.setStyleSheet(style)
        self.setLayout(grid)

    def calculate(self):
        amount = float(self.amount_line_edit.text())
        rate = float(self.rate_dbl_spinbox.text())
        vat = self.vat_percent_spinbox.text().strip("%")
        vat = float(vat) / 100 + 1.0
        no_vat = round(amount / rate / vat, 2)
        with_vat = round(amount / rate, 2)

        self.no_vat_label_result.setText(str(no_vat))
        self.vat_label_result.setText(str(with_vat))
        self.vat_label.setVisible(True)
        self.vat_label_result.setVisible(True)
        self.no_vat_label.setVisible(True)
        self.no_vat_label_result.setVisible(True)
        self.copy_vat_button.setVisible(True)
        self.copy_no_vat_button.setVisible(True)

    def copy_vat(self):
        pass

    def copy_no_vat(self):
        pass


app = QApplication(sys.argv)
calc = LaundryCalculator()
calc.show()
sys.exit(app.exec())
