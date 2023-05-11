import PySimpleGUI as sg

FUEL_TYPES = ['Petrol', 'Diesel']
# THEMES = {'Dark': 'Dark', 'Light': 'LightGreen'}

def create_window():
    layout = [[sg.Text('Fuel Purchasing App', font='Any 15', text_color='blue')],
              [sg.Text('Fuel type:', font='Any 12'), sg.Combo(FUEL_TYPES, key='fuel_type', font='Any 12', size=10)],
              [sg.Text('Quantity (Liters):', font='Any 12'), sg.Input(key='quantity', font='Any 12', size=10, enable_events=True)],
              [sg.Text('Price per liter in GHS:', font='Any 12'), sg.Input(key='price', font='Any 12', size=10, enable_events=True)],
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
            fuel_type = values['fuel_type']
            quantity = float(values['quantity'])
            price = float(values['price'])
            payment = values['payment']
            total_cost = quantity * price
            window['total_cost'].update(total_cost)

            # Save receipt
            receipt = {'Fuel Type': fuel_type, 'Quantity': quantity, 'Price': price, 'Payment Method': payment,
                       'Total Cost': total_cost}
            with open('receipts.txt', 'a') as f:
                f.write(str(receipt) + '\n')
        elif event == 'Recent Purchases':
            try:
                with open('receipts.txt', 'r') as f:
                    receipts = f.readlines()
                sg.popup('Recent Purchases', '\n'.join(receipts), font='Any 12')
            except:
                sg.popup('Error', 'No recent purchases', font='Any 12')
        elif event == 'quantity':
            quantity_input = window['quantity']
            try:
                quantity = float(quantity_input.get())
                if quantity <= 0:
                    raise ValueError('Invalid quantity.')
            except ValueError as e:
                quantity_input.update('')
                sg.popup_error(str(e), font='Any 12')
        elif event == 'price':
            price_input = window['price']
            try:
                price = float(price_input.get())
                if price <= 0:
                    raise ValueError('Invalid price.')
            except ValueError as e:
                price_input.update('')
                sg.popup_error(str(e), font='Any 12')

    window.close()