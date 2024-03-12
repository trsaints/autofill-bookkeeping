from autofill import fill_form
from arg_processor import get_args
from window_controller import switch_window


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
