from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QPushButton,
                             QComboBox, QSpinBox, QDoubleSpinBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent, QKeySequence
import sys


class LaundryCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Calculator")
        self.setMaximumSize(440, 200)
        grid = QGridLayout()

        # set stylesheet for elements
        currency_combobox_style = """
            margin-top: 7px;
            padding: 4px 10px 4px 10px;
            font-weight: bold;
            font-size: 18px;
        """
        vat_label_style = """
            margin-top: 50px;
            font-size: 22px;
        """
        no_vat_label_style = """
            font-size: 22px;
        """
        button_style = """
            padding: 10px 10px;
            font-size: 22px;
            font-weight: bold;
        """
        top_copy_button_style = """
            margin-top: 50px;
            font-weight: bold;
            padding: 6px 6px;
        """
        bottom_copy_button_style = """
            font-weight: bold;
            padding: 6px 6px;
        """

        base_style = """
            font-size: 22px;
            margin-top: 7px;
        """
        self.setStyleSheet(base_style)

        # create and add widgets
        rate_label = QLabel("Rate:")
        rate_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.rate_dbl_spinbox = QDoubleSpinBox()
        self.rate_dbl_spinbox.setRange(0.0, 10.0)
        self.rate_dbl_spinbox.setSingleStep(0.01)
        self.rate_dbl_spinbox.setValue(3.7)
        self.rate_dbl_spinbox.valueChanged.connect(self.calculate)
        grid.addWidget(rate_label, 0, 0)
        grid.addWidget(self.rate_dbl_spinbox, 0, 1)

        self.vat_percent_spinbox = QSpinBox()
        self.vat_percent_spinbox.setRange(0, 200)
        self.vat_percent_spinbox.setSingleStep(1)
        self.vat_percent_spinbox.setSuffix("% VAT")
        self.vat_percent_spinbox.setValue(17)
        self.vat_percent_spinbox.setMaximumWidth(140)
        self.vat_percent_spinbox.valueChanged.connect(self.calculate)
        grid.addWidget(self.vat_percent_spinbox, 0, 2)

        value_label = QLabel("Value:")
        value_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.value_dbl_spinbox = QDoubleSpinBox()
        self.value_dbl_spinbox.setRange(0.0, 10000000)
        self.value_dbl_spinbox.setSingleStep(40.0)
        self.value_dbl_spinbox.setValue(0)
        self.value_dbl_spinbox.valueChanged.connect(self.calculate)
        grid.addWidget(value_label, 1, 0)
        grid.addWidget(self.value_dbl_spinbox, 1, 1)

        currency_options = ["ILS", "USD"]
        self.currency_combobox = QComboBox()
        self.currency_combobox.addItems(currency_options)
        self.currency_combobox.currentIndexChanged.connect(self.calculate)
        self.currency_combobox.setStyleSheet(currency_combobox_style)
        self.currency_combobox.setMaximumWidth(140)
        grid.addWidget(self.currency_combobox, 1, 2, 1, 2)

        self.vat_label = QLabel("+VAT:")
        self.vat_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.vat_label.setStyleSheet(vat_label_style)
        self.vat_label_result = QLabel()
        self.vat_label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vat_label_result.setStyleSheet(vat_label_style)
        self.vat_label_result.setText("0.0 USD")
        grid.addWidget(self.vat_label, 3, 0)
        grid.addWidget(self.vat_label_result, 3, 1)

        self.copy_vat_button = QPushButton("Copy")
        self.copy_vat_button.clicked.connect(self.copy_vat)
        self.copy_vat_button.pressed.connect(self.copy_vat)
        self.copy_vat_button.setStyleSheet(top_copy_button_style)
        grid.addWidget(self.copy_vat_button, 3, 2)

        self.no_vat_label = QLabel("- VAT:")
        self.no_vat_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.no_vat_label.setStyleSheet(no_vat_label_style)
        self.no_vat_label_result = QLabel()
        self.no_vat_label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.no_vat_label_result.setText("0.0 USD")
        grid.addWidget(self.no_vat_label, 4, 0)
        grid.addWidget(self.no_vat_label_result, 4, 1)

        self.copy_no_vat_button = QPushButton("Copy")
        self.copy_no_vat_button.clicked.connect(self.copy_no_vat)
        self.copy_no_vat_button.pressed.connect(self.copy_no_vat)
        self.copy_no_vat_button.setStyleSheet(bottom_copy_button_style)
        grid.addWidget(self.copy_no_vat_button, 4, 2)

        self.setLayout(grid)

    def calculate(self):
        value = float(self.value_dbl_spinbox.text())
        rate = float(self.rate_dbl_spinbox.text())
        vat = self.vat_percent_spinbox.text().split("%")[0]

        if self.currency_combobox.currentText() == "ILS":
            vat = float(vat) / 100 + 1.0
            no_vat = round(value / rate / vat, 2)
            with_vat = round(value / rate, 2)
            self.no_vat_label_result.setText(f"{no_vat} USD")
            self.vat_label_result.setText(f"{with_vat} USD")
        else:
            vat = float(vat) / 100 + 1.0
            no_vat = round(value * rate / vat, 2)
            with_vat = round(value * rate, 2)
            self.no_vat_label_result.setText(f"{no_vat} ILS")
            self.vat_label_result.setText(f"{with_vat} ILS")

    def copy_vat(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.vat_label_result.text().split(" ")[0])

    def copy_no_vat(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.no_vat_label_result.text().split(" ")[0])


app = QApplication(sys.argv)
laundry_calc = LaundryCalculator()
laundry_calc.show()
sys.exit(app.exec())
