# try:
#     age = int (input('age: '))
#     print (age)
# except ValueError:
#     print ('invalid value, input int please')

try:
    faveNum = int (input('Favorite num: '))
    division = 10 / faveNum
    
    print (f" 10 divided by {faveNum} is: {division}")
except ValueError:
    print ('invalid value, input int please')
except ZeroDivisionError:
    print ("do not try number 0 again")