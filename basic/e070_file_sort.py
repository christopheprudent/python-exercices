import os
from pathlib import Path
import glob

# see: https://stackoverflow.com/questions/168409/how-do-you-get-a-directory-listing-sorted-by-creation-date-in-python

# get all .py files (of current directory)
files = glob.glob('*.py')
# sort by modification date
files = sorted(files, key=os.path.getmtime)
print(files)
