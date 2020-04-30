from subprocess import Popen

password=input("enter your password")
if(password=='pavi'):
    Popen('explorer')
else:
    print('enter the password correctly')


