def hello(name = 'Jose'):
    print('The hello() function has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello!'
    def welcome():
        return '\tThis is welcome inside hello()'
    
    
    print('I am going to return a function')
    
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')

print(my_new_func() )

def cool():
    
    def supercool():
        return 'I am very cool!'
    
    return supercool

some_func = cool()
print(some_func)
print(some_func())

def new_decorator(ogfunc):
    
    def wrap_func():
        print('Some extra code, before the original function')
        ogfunc
        print('Some extra code, after the original function!')
        
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')
    
func_needs_decorator()
decorated_func = new_decorator(func_needs_decorator)
decorated_func()
