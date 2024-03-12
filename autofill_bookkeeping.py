from pywinauto.application import Application
from autofill import fill_form
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start_date', required=True, type=str)
    parser.add_argument('-e', '--end_date', required=True, type=str)
    parser.add_argument('-t', '--fill_type', required=True, type=str)

    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date
    fill_type = args.fill_type

    return [start_date, end_date, fill_type]


def switch_window(window_name):
    try:
        print(f'Accessing window {window_name}...')
        app = Application().connect(title=window_name)
        app.window().set_focus()
    except Exception as e:
        print(
            f'Could not access window due to the following: {e.with_traceback()}')


def initialize():
    args = get_args()
    [start_date, end_date, fill_type] = args

    print('starting automation...')

    try:
        switch_window('Sem título - Bloco de Notas')
        fill_form(start_date, end_date, fill_type, False)
    except Exception as e:
        print(f'Failed to fill form due to error: {e.with_traceback()}')

    print('process finished')


initialize()
