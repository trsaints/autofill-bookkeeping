from pywinauto.application import Application
from autofill import fill_form


def switch_window(window_name):
    try:
        print(f'Accessing window {window_name}...')
        app = Application().connect(title=window_name)
        app.window().set_focus()
    except Exception as e:
        print(
            f'Could not access window due to the following: {e.with_traceback()}')


def initialize():
    print('starting automation...')

    switch_window('Sem título - Bloco de Notas')

    try:
        fill_form('01/03/2025', '01/04/2025', 'NF-e', False)
    except Exception as e:
        print(f'Error while filling form: {e.with_traceback()}')

    print('process finished')


initialize()
