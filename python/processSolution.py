# processSolution.py

import tools
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--challenge_date",         "-d", default="", help="Challenge date (YYYY-MM-DD)")
    parser.add_argument("--programming_language",   "-l", default="", help="Programming language")

    options                 = parser.parse_args()
    challenge_date          = options.challenge_date
    programming_language    = options.programming_language

    solution_file   = "undefined.txt"
    # Make home directory general to work for any user
    download_dir    = "/Users/caleb/Downloads"
    
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

if __name__ == "__main__":
    main()
