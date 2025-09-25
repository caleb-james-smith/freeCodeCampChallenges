# freeCodeCampChallenges

Solutions to daily coding challenges from freeCodeCamp (fCC).

https://www.freecodecamp.org/learn/daily-coding-challenge/archive

If you download your solution from the fCC website,
it should be saved as `undefined.txt` in your Downloads folder.
However, a number will be added if this file already exists,
for example `undefined (1).txt`.

You may use the script `processSolution.py` to process the solution file `undefined.txt`.
The required inputs are the challenge date and programming language.
This script should create a directory for the programming language (if it does not exist),
move and rename the file with the challenge date and extension,
and remove extra lines that start and end with `**`.

```
python3 python/processSolution.py -d 2025-09-25 -l py
```
