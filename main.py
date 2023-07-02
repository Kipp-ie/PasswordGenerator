import random
import PySimpleGUI as sg

input_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '?']
input_special = ['!', '@', '#', '?']

layout = [
    [
        sg.Text('Password Generator'),
        [],
        sg.Button('Generate a password'),
        sg.Input(('Replace this with your service!'), key='-INPUT-')
    ]
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Generate a password':
        service = values['-INPUT-']
        b = random.randint(0, len(input_list) - 1)
        password = (input_list[b])
        b2 = random.randint(0, len(input_list) - 1)
        password2 = (input_list[b2])
        b3 = random.randint(0, len(input_list) - 1)
        password3 = (input_list[b3])
        b4 = random.randint(0, len(input_list) - 1)
        password4 = (input_list[b4])
        b5 = random.randint(0, len(input_list) - 1)
        password5 = (input_list[b5])
        b6 = random.randint(0, len(input_list) - 1)
        password6 = (input_list[b6])
        b7 = random.randint(0, len(input_list) - 1)
        password7 = (input_list[b7])
        b8 = random.randint(0, len(input_list) - 1)
        password8 = (input_list[b8])
        b9 = random.randint(0, len(input_list) - 1)
        password9 = (input_list[b9])
        b10 = random.randint(0, len(input_list) - 1)
        password10 = (input_list[b10])
        b11 = random.randint(0, len(input_list) - 1)
        password11 = (input_list[b11])
        b12 = random.randint(0, len(input_list) - 1)
        password12 = (input_list[b12])
        b13 = random.randint(0,len(input_special) - 1)
        password13 = (input_special[b13])

        passwordcombo = password+password2+password3+password4+password5+password6+password7+password8+password8+password9+password10+password11+password12+password13





    if service:
        sg.Popup('Service: ' + service, f"Password: {passwordcombo}", 'Password saved in the text document')
        with open('password.txt', 'a') as f:
            f.write("\n--------------------------\n" "Service: " + service + '\n' 'Password: ' + passwordcombo + '\n--------------------------')
            f.write('\n')








