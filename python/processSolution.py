# processSolution.py

import tools
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--challenge_date", "-d", default="", help="Challenge date (YYYY-MM-DD)")
    parser.add_argument("--language",       "-l", default="", help="Programming language")

    options         = parser.parse_args()
    challenge_date  = options.challenge_date
    language        = options.language

    solution_file   = "undefined.txt"
    # Make home directory general to work for any user
    download_dir    = "/Users/caleb/Downloads"
    
    if not challenge_date:
        print("Please provide a challenge date (YYYY-MM-DD) using the -d option.")
        sys.exit(1)

    if not language:
        print("Please provide a programming language using the -l option.")
        sys.exit(1)

    if language == "py":
        language = "python"

    if language == "js":
        language = "javascript"

    processSolution(solution_file, download_dir, challenge_date, language)

def processSolution(solution_file, download_dir, challenge_date, language):
    code_dir    = language
    extension   = tools.getExtension(language)
    
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
