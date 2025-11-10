try:
    100/0 #As zero division error is defined exception will get caught in ZeroDivisionError
    #raise ValueError #As ValueError is not defined in exception block it will be caught by general except block
except ZeroDivisionError:
    print(f'caught zero division exception.')
except:
    print(f'caught general error')