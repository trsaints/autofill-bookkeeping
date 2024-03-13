from pywinauto.application import Application


def switch_window(process_id):
    try:
        print(f'Accessing window via process {process_id}...')
        app = Application().connect(process=process_id)
        app.window().set_focus()
    except Exception as e:
        print(
            f'Could not access window due to the following: {e.with_traceback()}')
