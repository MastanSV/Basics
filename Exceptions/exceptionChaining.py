def classicExampleForEChainingWithoutFrom():
    try:
        x = 2 / 0
    except ZeroDivisionError as e:
        raise TypeError("from zero division error.")
#in the above example, from e is not used so implicit chaining will be mapped, so you can get that implicit chaining
#with __context__ dunder method.So Error message would follows below,
#During handling of the above exception, another exception occured:

def classicExampleForEChainingWithFrom():
    try:
        x = 2/0
    except ZeroDivisionError as e:
        raise TypeError("from zero division error.") from e
    
#In the second example, we have used from e method, which tells python that Map the ZeroDivisionError which is
#cause for raising TypeError. So Error would be as follows.
#The above exception was the direct cause of the following exception.

try:
    classicExampleForEChainingWithoutFrom()
except TypeError as e:
    print(f'cause for the exception context : {e.__context__}')


try:
    classicExampleForEChainingWithFrom()
except TypeError as e:
    print(f'cause for the exception cause : {e.__cause__}')
