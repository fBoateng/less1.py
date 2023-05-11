import PySimpleGUI as sg

FUEL_TYPES = ['Petrol', 'Diesel']
# THEMES = {'Dark': 'Dark', 'Light': 'LightGreen'}


'''def change_theme_event(window):
    theme = window['Change Theme'].metadata
    sg.change_look_and_feel(THEMES[theme])'''


def create_window():
    layout = [[sg.Text('Fuel Purchasing App', font='Any 15', text_color='blue')],
              [sg.Text('Fuel type:', font='Any 12'), sg.Combo(FUEL_TYPES, key='fuel_type', font='Any 12', size=10)],
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
        '''elif event == 'Change Theme':
            change_theme_event(window)'''

    window.close()


if __name__ == '__main__':
    sg.theme('DarkBlue')
    create_window()

'''This Python program uses the PySimpleGUI library to create a graphical user interface (GUI) for a fuel purchasing 
application. The GUI has fields for the user to enter the fuel type, quantity of fuel, price per liter, and payment 
method, and calculates the total cost of the fuel purchase. The user can also view a list of recent purchases and 
change the theme of the application.

The program starts by defining two constants: FUEL_TYPES, which is a list of the available fuel types (Petrol and 
Diesel), and THEMES, which is a dictionary of the available themes (Dark and Light).

The create_window() function defines the layout of the GUI using the PySimpleGUI API. It creates a window with a 
title, text labels, input fields, buttons, and a text field to display the total cost of the fuel purchase. It also 
defines an event loop that waits for the user to interact with the GUI and respond to the user's actions.

The event loop listens for the user to click on one of the buttons, such as 'Purchase' or 'Recent Purchases', 
and responds accordingly. When the 'Purchase' button is clicked, the program reads the input fields, calculates the 
total cost of the fuel purchase, and writes the purchase information to a file. When the 'Recent Purchases' button is 
clicked, the program reads the file and displays a list of recent purchases in a pop-up window.

The change_theme_event() function handles the 'Change Theme' button by changing the color scheme of the GUI based on 
the user's selection.

The main block of the program sets the theme of the GUI, calls the create_window() function, and runs the event loop 
until the user closes the window or clicks the 'Cancel' button.'''
