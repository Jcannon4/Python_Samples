try:
    f = open('testfile','r') #change to 'w' to avoid error
    f.write('Write a test line')
except TypeError:
    print('There was a type Error!')
except OSError:
   print('Hey you have an OS Error')
except:
    print('All other exceptions!')
finally:
    print('I always run')
    
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops that is not a number')
            continue
        else:
            print('Yes Thank You')
            break
        finally:
            print('End of try/except/finally')
            print("I will always run!")
ask_for_int()

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Type Error')
    
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('DONT EVER DIVIDE BY ZERO!!!')

def ask():
    while True:
        try:
            kawhi = int(input('Square a number: '))
            print(str(kawhi) + ' squared is ' + str(kawhi**2))
        except:
            print('Thats not a number!')
            continue
        finally:
            print('Not sure what useful statement to put here')
        break
ask()