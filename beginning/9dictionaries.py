# هر عددی  رو به حروفش برمیگردونه
num = input ("inter a number you want:  ")

numbers = {
    "1":"one ",
    "2":"two ",
    "3":"three ",
    "4":"four ",
    "5":"five ",
    "6":"six ",
    "7":"seven ",
    "8":"eight ",
    "9":"nine "
}
output=""
for ch in num:
    output += numbers.get(ch,"error accured")

print (output)
