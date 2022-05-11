import glob

# searchs for all files that end in the python extension py in the current directory
for py in glob.glob("*.py"):
    print(py)
