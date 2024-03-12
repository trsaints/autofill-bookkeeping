import pyautogui
import datetime
from time import sleep
from dateutil.relativedelta import relativedelta


def fill_form(start_date, end_date, fill_type, dev_mode=False):
    # Convert strings to date objects
    start_date_object = datetime.datetime.strptime(start_date, '%d/%m/%Y')
    end_date_object = datetime.datetime.strptime(end_date, '%d/%m/%Y')

    # Loop from start_date to end_date
    current_date = start_date_object

    while current_date <= end_date_object:
        if not dev_mode:
            sleep(1)

        print(f'Filling form for {current_date.strftime("%d/%m/%Y")}...')

        pyautogui.hotkey('ctrl', 'insert')
        pyautogui.press('tab')
        pyautogui.typewrite(fill_type + ' - ' +
                            current_date.strftime('%d/%m/%Y'))
        pyautogui.press('tab', presses=3)
        pyautogui.press('down')
        pyautogui.press('tab', presses=4)
        pyautogui.typewrite('1')
        pyautogui.press('tab', presses=3)
        pyautogui.typewrite('1')
        pyautogui.press('tab', presses=3)
        pyautogui.typewrite(current_date.strftime('%d/%m/%Y'))
        pyautogui.press('tab')
        pyautogui.typewrite(current_date.strftime('%d/%m/%Y'))
        pyautogui.press('tab')
        pyautogui.typewrite('000000000000000')
        pyautogui.press('tab')
        pyautogui.typewrite('999999999999999')
        pyautogui.press('tab')
        if fill_type == 'NFS-e':
            pyautogui.typewrite('2216')
        pyautogui.press('tab', presses=5)
        pyautogui.press('enter')

        # Increase current_date by one day
        current_date += relativedelta(days=+1)
