from pywinauto.application import Application


def switch_window(window_name):
    try:
        print(f'Accessing window {window_name}...')
        app = Application().connect(title=window_name)
        app.window().set_focus()
    except Exception as e:
        print(
            f'Could not access window due to the following: {e.with_traceback()}')
