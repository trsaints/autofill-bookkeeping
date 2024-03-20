import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start_date', required=True, type=str)
    parser.add_argument('-e', '--end_date', required=True, type=str)
    parser.add_argument('-t', '--fill_type', required=True, type=str)
    parser.add_argument('-p', '--pid', required=True, type=int)
    parser.add_argument('-d', '--dev_mode', action='store_true')

    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date
    fill_type = args.fill_type
    pid = args.pid
    dev_mode = args.dev_mode

    return [start_date, end_date, fill_type, pid, dev_mode]
