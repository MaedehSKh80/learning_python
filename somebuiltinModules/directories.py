from pathlib import Path

# if the directory exist or not?
path = Path('packagePractice')
print (path.exists())


# making directory
# pathEmails = Path ('emails')
# print(pathEmails.mkdir())

# removing directory
# pathEmails = Path ('emails')
# print(pathEmails.rmdir())



# all the files and directories in the path
# path = Path ()
# print(path.glob('*.'))

# * means everything
# *.* means all the files
# *.py means all the python files


# هر فابل پایتونی ببینه اسمشو پرینت میکنه:
path = Path()
for file in path.glob('*.py'):
    print(file)


