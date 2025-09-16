# processSolution.py

import sys

def processSolution(solution_file, download_dir, language):
    code_dir    = getCodeDir(language)
    extension   = getExtension(language)

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

def main():
    solution_file   = "undefined.txt"
    download_dir    = "/Users/caleb/Downloads"
    language        = "C++"

    processSolution(solution_file, download_dir, language)
    
if __name__ == "__main__":
    main()
