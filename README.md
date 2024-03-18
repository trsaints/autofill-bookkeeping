# Autofill Bookkeeping

The purpose of this project is to automate the form filling process in a specific ERP system.

## Topics

- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgements](#acknowledgments)
- [Usage](#usage)

## Dependencies

This project uses the following libraries:

1. [pyautogui](https://github.com/asweigart/pyautogui)

   - Copyright (c) 2014, Al Sweigart
   - All rights reserved.
   - Licensed under the BSD 3-Clause "New" or "Revised" License

2. [pywinauto](https://github.com/pywinauto/pywinauto)
   - Copyright (c) 2017, Mark Mc Mahon and Contributors
   - All rights reserved.
   - Licensed under the BSD 3-Clause "New" or "Revised" License

## License

This project is licensed under the BSD 3-Clause "New" or "Revised" License.

## Acknowledgments

- Thanks to Al Sweigart and Mark Mc Mahon and Contributors for their wonderful libraries.

## Usage

Open the project directory and type the following command in your shell environment:

```shell
py 'autofill_bookkeeping.py' -p $PID -s $START_DATE -e $END_DATE -t $FILL_TYPE
```

The command accepts the following parameters:

- `-p`: Specifies the PID (Process ID) for the form filling process.
- `-s`: Specifies the start date for the form filling process.
- `-e`: Specifies the end date for the form filling process.
- `-t`: Specifies the fill type for the form filling process.

Make sure to replace `$PID`, `$START_DATE`, `$END_DATE`, and `$FILL_TYPE` with the actual values you want to use.
