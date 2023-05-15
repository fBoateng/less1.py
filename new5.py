import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout

FUEL_TYPES = ['Petrol', 'Diesel']

def validate_input(values):
    quantity = float(values['quantity'])
    if quantity <= 0:
        raise ValueError('Invalid quantity.')

    price = float(values['price'])
    if price <= 0:
        raise ValueError('Invalid price.')

    return quantity, price

def save_receipt(receipt):
    with open('receipts.txt', 'a') as f:
        f.write(str(receipt) + '\n')

def get_recent_purchases():
    with open('receipts.txt', 'r') as f:
        receipts = f.readlines()
    return receipts

def close_window():
    app.quit()

def create_window():
    window = QWidget()
    window.setWindowTitle('Fuel Purchasing App')

    label_fuel_type_name = QLabel(text='Fuel type name:')
    combobox_fuel_type_name = QComboBox()
    combobox_fuel_type_name.addItems(FUEL_TYPES)

    label_quantity = QLabel(text='Quantity (Liters):')
    entry_quantity = QLineEdit()

    label_price = QLabel(text='Price per liter in GHS:')
    entry_price = QLineEdit()

    label_payment_method = QLabel(text='Payment method:')
    combobox_payment_method = QComboBox()
    combobox_payment_method.addItems(FUEL_TYPES)

    label_total_cost = QLabel(text='Total Cost:')
    label_total_cost_value = QLabel()

    button_purchase = QPushButton(text='Purchase')
    button_recent_purchases = QPushButton(text='Recent Purchases')
    button_cancel = QPushButton(text='Cancel')

    layout = QVBoxLayout()
    layout.addWidget(label_fuel_type_name)
    layout.addWidget(combobox_fuel_type_name)

    layout.addWidget(label_quantity)
    layout.addWidget(entry_quantity)

    layout.addWidget(label_price)
    layout.addWidget(entry_price)

    layout.addWidget(label_payment_method)
    layout.addWidget(combobox_payment_method)

    layout.addWidget(label_total_cost)
    layout.addWidget(label_total_cost_value)

    layout.addWidget(button_purchase)
    layout.addWidget(button_recent_purchases)
    layout.addWidget(button_cancel)

    window.setLayout(layout)

    def purchase():
        try:
            quantity, price = validate_input(values)
            total_cost = quantity * price
            label_total_cost_value.setText(str(total_cost))
            receipt = {'Fuel Type': combobox_fuel_type_name.currentText(), 'Quantity': quantity, 'Price': price, 'Payment Method': payment_method.currentText(),
                       'Total Cost': total_cost}
            save_receipt(receipt)
        except ValueError as e:
            QMessageBox.critical(window, 'Error', str(e))

    def recent_purchases():
        receipts = get_recent_purchases()
        if receipts:
            QMessageBox.information(window, 'Recent Purchases', '\n'.join(receipts))
        else:
            QMessageBox.information(window, 'Error', 'No recent purchases')

    def close():
        app.quit()

    button_purchase.clicked.connect(purchase)
    button_recent_purchases.clicked.connect(recent_purchases)
    button_cancel.clicked.connect(close)

    window.show()

    return window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = create_window()
