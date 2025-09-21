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

# get file extension based on programming language
def getExtension(programming_language):
    result = None
    extensions = {
        "python"        : "py",
        "javascript"    : "js"
    }
    try:
        result = extensions[programming_language]
    except KeyError:
        print(f"KeyError in getExtension: Did not find the programming language '{programming_language}'.")
        sys.exit(1)
    
    return result

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

# add date to file name
def addDateToFileName(original_file_name):
    print("Adding date to file name...")

    today_date = getTodayDate()
    today_date = today_date.replace("-", "_")
    file_base, file_extension = os.path.splitext(original_file_name)
    new_file_name = f"{file_base}_{today_date}{file_extension}"
    
    print(f" - today's date: {today_date}")
    print(f" - original file name: {original_file_name}")
    print(f" - new file name: {new_file_name}")
    
    return new_file_name
