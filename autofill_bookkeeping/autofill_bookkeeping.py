from autofill import auto_fill
from arg_processor import get_args
from window_controller import switch_window


def initialize():
    args = get_args()
    [start_date, end_date, fill_type, pid, dev_mode] = args

    try:
        switch_window(pid)
        auto_fill(start_date, end_date, fill_type, dev_mode)
    except Exception as e:
        print(f'Failed to fill form due to error: {e.with_traceback()}')


initialize()
