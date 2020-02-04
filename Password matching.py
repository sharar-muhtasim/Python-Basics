#program that exits if you type the wrong password
import sys
password = '12345678'
print('Enter password:')
typed_pass = input()
if typed_pass != password:
    sys.exit()
else:
    print('Password matched')