# tools.py

import os
import sys
import shutil
import datetime

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# move file if it exists; if not, print error and exit
def moveFile(source_file, destination_file):
    print("Moving file...")
    print(f" - source file: {source_file}")
    print(f" - destination file: {destination_file}")
    try:
        shutil.move(source_file, destination_file)
    except FileNotFoundError:
        print(f"ERROR: Cannot move the file '{source_file}' as it was not found.")
        sys.exit(1)

# append slash to path if path does not end in slash
def appendSlash(path):
    slash = "/"
    if path[-1] != slash:
        path += slash
    return path

# get today's date
def getTodayDate(date_format="%Y-%m-%d"):
    today_date_object = datetime.datetime.today()
    today_date = today_date_object.strftime(date_format)
    return today_date
