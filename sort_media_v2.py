import os
from datetime import datetime
import shutil
import argparse

parser = argparse.ArgumentParser(description="Sort photos/videos given into folders by years/months")
parser.add_argument("input_dir", help="A path to directory containing photos/videos to be sorted", type=str)
parser.add_argument("-o", "--output_dir", help="A path to directory to store the sorted folders of photos/videos",
                    type=str)
temp_list = []


# Helper function to convert time to UTC form
def convert_date(epochtime):
    utc_time = datetime.utcfromtimestamp(epochtime)
    created_month = utc_time.strftime('%b')
    created_year = utc_time.strftime('%Y')
    return created_year, created_month


# helper function to scan through the input folder, form a list of year/month sub-directories need to be created.
def scan_create_subdir(input_dir, output_dir):
    files = os.scandir(input_dir)
    for file in files:
        if file.is_file():
            info = file.stat()
            year_month = convert_date(info.st_mtime)
            print(year_month)  # DEBUG
            if year_month not in temp_list:
                temp_list.append(year_month)
    print(temp_list)  # DEBUG
    for year_month in temp_list:
        try:
            os.makedirs(output_dir + '/' + year_month[0] + '/' + year_month[1] + '/')
        except FileExistsError as exc:
            print(exc)
    return


def sort_media(input_dir, output_dir):
    files = os.scandir(input_dir)
    for file in files:
        if file.is_file():
            info = file.stat()
            year_month = convert_date(info.st_mtime)
            shutil.move(input_dir + '/' + file.name, output_dir + '/' + year_month[0] + '/' + year_month[1] + '/')


def main():
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    # DEBUG
    print(input_dir)
    print(output_dir)
    scan_create_subdir(input_dir, output_dir)
    sort_media(input_dir, output_dir)


if __name__ == '__main__':
    main()
