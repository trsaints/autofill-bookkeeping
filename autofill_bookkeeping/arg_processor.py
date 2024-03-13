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
