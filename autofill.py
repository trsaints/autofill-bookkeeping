import pyautogui
import datetime
from time import sleep
from dateutil.relativedelta import relativedelta


def get_date_objects(start_date, end_date):
    start_date_object = datetime.datetime.strptime(start_date, '%d/%m/%Y')
    end_date_object = datetime.datetime.strptime(end_date, '%d/%m/%Y')

    return [start_date_object, end_date_object]


def fill_entry_name(fill_type, current_date):
    pyautogui.press('tab')
    pyautogui.typewrite(fill_type + ' - ' +
                        current_date.strftime('%d/%m/%Y'))


def fill_entry_type():
    pyautogui.press('tab', presses=3)
    pyautogui.press('down')


def fill_affiliate():
    pyautogui.press('tab', presses=4)
    pyautogui.typewrite('1')
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite('1')
    pyautogui.press('tab', presses=3)


def fill_period(current_date):
    pyautogui.typewrite(current_date.strftime('%d/%m/%Y'))
    pyautogui.press('tab')
    pyautogui.typewrite(current_date.strftime('%d/%m/%Y'))
    pyautogui.press('tab')


def fill_receipt_id_range():
    pyautogui.typewrite('000000000000000')
    pyautogui.press('tab')
    pyautogui.typewrite('999999999999999')
    pyautogui.press('tab')


def fill_entry_code(fill_type):
    if fill_type == 'NFS-e':
        pyautogui.typewrite('2216')

    pyautogui.press('tab', presses=5)
    pyautogui.press('enter')


def fill_form(start_date, end_date, fill_type, dev_mode=False):
    [start, end] = get_date_objects(start_date, end_date)

    print(f'Starting to fill form from {start_date} to {end_date}...')

    current_date = start

    while current_date <= end:
        if not dev_mode:
            sleep(1)

        print(f'Filling form for {current_date.strftime("%d/%m/%Y")}...')

        pyautogui.hotkey('ctrl', 'insert')

        fill_entry_name(fill_type, current_date)
        fill_entry_type()
        fill_affiliate()
        fill_period(current_date)
        fill_receipt_id_range()
        fill_entry_code(fill_type)

        current_date += relativedelta(days=+1)

    print('Form filling complete.')
