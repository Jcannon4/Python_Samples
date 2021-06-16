ex = list(range(0,10))

def create_cubes(n):
    
    results = []
    for c in range(n):
        results.append(c**3)
    return results
for x in create_cubes(10):
    print(x)

def gen_fibon(n):
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)

def simple_gen():
    for x in range(3):
        yield x
        
for number in simple_gen():
    print(number)

g = simple_gen()
g

#More Memory efficient this way to use yield rather than for loop
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) - will cause an error if ran because there is no more

s = 'hello'
for letter in s:
    print(letter)
s_iter = iter(s)
next(s_iter)