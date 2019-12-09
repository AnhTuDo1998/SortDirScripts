# A script to check for created time of files in a directory and convert them into human readable form with year
# and month information for scrip writing purpose

import os
from datetime import datetime
import shutil

listYearMonth = set()
basepath = 'C:/Users/Boom/OneDrive/Pictures/Camera Roll'

# Helper function to convert epoch time to month year
def convert_date(epochtime):
    utc_time = datetime.utcfromtimestamp(epochtime)
    created_month = utc_time.strftime('%b')
    created_year = utc_time.strftime('%Y')
    listYearMonth.add((created_year, created_month))
    create_subdir()
    return created_year, created_month

# Helper function to create sub directory for the year/ month
def create_subdir():
    for year_month in listYearMonth:
        try:
            os.makedirs(basepath + '/' + year_month[0] + '/' + year_month[1] + '/')
        except FileExistsError as exc:
            print(exc)

# Helper function to sort images into the correct directory
def sort_images(basepath):
    medium = os.scandir(basepath)
    for media in medium:
        if media.is_file():
            info = media.stat()
            year_month = convert_date(info.st_ctime)
            shutil.move(basepath + '/' + media.name, basepath +'/' + year_month[0] + '/' + year_month[1] + '/')



def __main__():
    sort_images(basepath)


if __name__ == "__main__":
    __main__()


