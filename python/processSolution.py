# processSolution.py

import tools
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--challenge_date",         "-d", default="", help="Challenge date (YYYY-MM-DD)")
    parser.add_argument("--programming_language",   "-l", default="", help="Programming language")

    options                 = parser.parse_args()
    challenge_date          = options.challenge_date
    programming_language    = options.programming_language

    home_dir = Path.home()

    solution_file   = "undefined.txt"
    download_dir    = f"{home_dir}/Downloads"
    
    if not challenge_date:
        print("Please provide a challenge date (YYYY-MM-DD) using the -d option.")
        sys.exit(1)

    if not programming_language:
        print("Please provide a programming language using the -l option.")
        sys.exit(1)

    programming_language = programming_language.lower()

    if programming_language == "py":
        programming_language = "python"

    if programming_language == "js":
        programming_language = "javascript"

    processSolution(solution_file, download_dir, challenge_date, programming_language)

def processSolution(solution_file, download_dir, challenge_date, programming_language):
    print("Processing solution file...")
    print(f" - solution_file: {solution_file}")
    print(f" - download_dir: {download_dir}")
    print(f" - challenge_date: {challenge_date}")
    print(f" - programming_language: {programming_language}")

    code_dir    = programming_language
    extension   = tools.getExtension(programming_language)
    
    download_dir    = tools.appendSlash(download_dir)
    code_dir        = tools.appendSlash(code_dir)

    challenge_date = challenge_date.replace("_", "-")
    new_file_name = f"challenge-{challenge_date}.{extension}"

    source_file         = download_dir + solution_file
    destination_file    = code_dir + new_file_name

    tools.makeDir(code_dir)
    tools.moveFile(source_file, destination_file)
    removeExtraLines(destination_file)

    print("Done!")

def removeExtraLines(file_name):
    print("Removing extra lines...")
    tag = "**"
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith(tag) and stripped_line.endswith(tag):
                print("Removing line:")
                print(line, end="")
                continue
            f.write(line)

if __name__ == "__main__":
    main()
