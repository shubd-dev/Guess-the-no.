import PySimpleGUI as sg
import random

num = random.randint(0,1000)
layout =[[sg.Text("Guess a Number", key='out', text_color= 'cyan',  font= '10')],
        [sg.Input(key='-INPU-')],
        [sg.Text(size=(35,3), key='OUTPUT')],
        [sg.Button('Guess'), sg.Button('Quit')]]

def correct(a):
    window['OUTPUT'].update("Bingo! You Guesses it right "+a+" was choosed.",text_color = '#C3FDB8', font= '10' )
def above(a):
    window['OUTPUT'].update("Way to above lower down a bit, not "+a, text_color = '#FDD017', font= '10')
def below(a):
    window['OUTPUT'].update("Tooo low up a notch, "+a+" is'nt I choosed", text_color = '#F70D1A', font= '10')
window = sg.Window('Guess', layout)

def game(a):
    if num == int(a):
        correct(a)
    if num < int(a):
        above(a)
    if num > int(a):
        below(a)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    game(values['-INPU-'])
window.close()
