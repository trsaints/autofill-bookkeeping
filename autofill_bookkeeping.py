from autofill import auto_fill
from arg_processor import get_args
from window_controller import switch_window


def initialize():
    args = get_args()
    [start_date, end_date, fill_type] = args

    try:
        switch_window('Sem título - Bloco de Notas')
        auto_fill(start_date, end_date, fill_type, False)
    except Exception as e:
        print(f'Failed to fill form due to error: {e.with_traceback()}')


initialize()
