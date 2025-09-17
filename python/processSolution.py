# processSolution.py

import tools
import sys

def main():
    solution_file   = "undefined.txt"
    download_dir    = "/Users/caleb/Downloads"
    challenge_date  = "2000-01-01"
    language        = "py"

    if language == "py":
        language = "python"

    if language == "js":
        language = "javascript"

    processSolution(solution_file, download_dir, challenge_date, language)

def processSolution(solution_file, download_dir, challenge_date, language):
    # If code_dir is always equal to language, we do not need getCodeDir(language).
    code_dir    = getCodeDir(language)
    extension   = getExtension(language)
    
    download_dir    = tools.appendSlash(download_dir)
    code_dir        = tools.appendSlash(code_dir)

    challenge_date = challenge_date.replace("_", "-")
    new_file_name = f"challenge-{challenge_date}.{extension}"

    source_file         = download_dir + solution_file
    destination_file    = code_dir + new_file_name

    tools.makeDir(code_dir)
    tools.moveFile(source_file, destination_file)

def getCodeDir(language):
    result = None
    directories = {
        "python"        : "python",
        "javascript"    : "javascript"
    }
    try:
        result = directories[language]
    except KeyError:
        print(f"KeyError in getCodeDir: Did not find the language '{language}'.")
        sys.exit(1)
    
    return result

def getExtension(language):
    result = None
    extensions = {
        "python"        : "py",
        "javascript"    : "js"
    }
    try:
        result = extensions[language]
    except KeyError:
        print(f"KeyError in getExtension: Did not find the language '{language}'.")
        sys.exit(1)
    
    return result

if __name__ == "__main__":
    main()
