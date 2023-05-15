import PySimpleGUI as sg

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
    window.close()

def create_window():
    layout = [[sg.Text('Fuel Purchasing App', font='Any 15', text_color='blue')],
              [sg.Text('Fuel type name:', font='Any 12'), sg.Combo(FUEL_TYPES, key='fuel_type_name', font='Any 12', size=10)],
              [sg.Text('Quantity (Liters):', font='Any 12'), sg.Input(key='quantity', font='Any 12', size=10)],
              [sg.Text('Price per liter in GHS:', font='Any 12'), sg.Input(key='price', font='Any 12', size=10)],
              [sg.Text('Payment method:', font='Any 12'), sg.Combo(['Cash', 'Card'], key='payment', font='Any 12')],
              [sg.Text('Total Cost:', font='Any 12'), sg.Text('', key='total_cost', font='Any 12')],
              [sg.Button('Purchase', font='Any 12'), sg.Button('Recent Purchases', font='Any 12'),
               sg.Button('Cancel', font='Any 12')],

              ]

    window = sg.Window('Fuel Purchasing App', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event == 'Purchase':
            try:
                quantity, price = validate_input(values)
                total_cost = quantity * price
                window['total_cost'].update(total_cost)
                receipt = {'Fuel Type': fuel_type_name, 'Quantity': quantity, 'Price': price, 'Payment Method': payment,
                       'Total Cost': total_cost}
                save_receipt(receipt)
            except ValueError as e:
                sg.popup_error(str(e), font='Any 12')
                continue

        elif event == 'Recent Purchases':
            receipts = get_recent_purchases()
            if receipts:
                sg.popup('Recent Purchases', '\n'.join(receipts), font='Any 12')
            else:
                sg.popup('Error', 'No recent purchases', font='Any 12')

    window.close()

if __name__ == '__main__':
    create_window()
