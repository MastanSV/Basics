try:
    x = 10/2
    #open('invalidfile.txt')
except (FileNotFoundError, PermissionError) as e:
    print(f'Error caught: {e.args}')
else: # else block will run only when after successful execution of try block
    print('Successful excution of try block') 
finally:
    print('will run always')


#scenario without except block
try:
    x = 10/2
finally:
    print('valid')