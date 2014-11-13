#! /usr/bin/env python


#= random ================================================
r = random.randint(0, RAND_POS)


#= real ================================================
round(pi, i)

#= dict ================================================
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel.keys()
['guido', 'irv', 'jack']
>>> 'guido' in tel
True

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}

>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
#= sets ================================================
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
set(['r', 'd'])
#= tuple ================================================
t = 12345, 54321, 'hello!'
v = ([1, 2, 3], [3, 2, 1])
u = t, (1, 2, 3, 4, 5)
singleton = 'hello',
 x, y, z = t
#= list ================================================
# method
>>> stack = [3, 4, 5]
>>> stack.append(7)
>>> stack.pop()
list.append(x)
list.extend(L)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.index(x)
list.count(x)
list.sort(cmp=None, key=None, reverse=False)
list.reverse()

# map
>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> filter(f, range(2, 25))

>>> def cube(x): return x*x*x
>>> map(cube, range(1, 11))
>>> seq = range(8)
>>> def add(x, y): return x+y
>>> map(add, seq, seq)

>>> def add(x,y): return x+y
>>> reduce(add, range(1, 11))

# comprehension
squares = [x**2 for x in range(10)]

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]

>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]

#
>>> [[row[i] for row in matrix] for i in range(4)]
zip(*matrix)

del a[0]
del a[2:4]
del a[:]
del a


#= list loop ================================================
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print i, v

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)

>>> for i in reversed(xrange(1,10,2)):
...     print i

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print f

>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():

>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
#= if ================================================
>>> x = int(raw_input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
... elif x == 0:
...     print 'Single'
... else:
...     print 'More'
...
#= for ================================================
range(5, 10)
range(0, 10, 3)
range(-10, -100, -30)
for w in words:
    print w, len(w)

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

for i in range(len(a)):
    print i, a[i]
    break
    continue
    pass
#= function =================================================
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f = fib
f(100)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):

def cheeseshop(kind, *arguments, **keywords): # *arg : tuple    **arg : dict
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
arg1=[1,2,3]
arg2={1:2, 2:3, 3:4}
cheeseshop(1, *arg1, **arg2)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print my_function.__doc__

#= input output ================================================
# print
str()
repr()
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)
for x in range(1,11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'

print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print 'The value of PI is approximately %5.3f.' % math.pi


# file
f = open('workfile', 'w')
f.read(size)
f.read()
f.readline()
for line in f:
    print line,
list(f)
f.readlines()

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
f.write(s)

f = open('workfile', 'r+')
f.write('0123456789abcdef')
f.seek(5)     # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2) # Go to the 3rd byte before the end
f.read(1)
f.close()

with open('workfile', 'r') as f:
    read_data = f.read()
f.closed

# json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
#= exception ================================================
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
else:
    f.close()

try:
    this_fails()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
#= statements ================================================
>>> x = int(raw_input("Please enter an integer: "))
sys.argv[1:]
#= module ================================================
import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__
fib = fibo.fib
fib(500)
from fibo import fib, fib2
from fibo import *
fib(500)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

print sys.path
print dir(fibo)
print dir(sys)
print dir()
print dir(__builtin__)
#= package ================================================
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

__init__.py:
__all__ = ["echo", "surround", "reverse"]
import sound.effects.echo
from sound.effects import echo
from sound.effects import *  # import from __all__

#= calss ================================================
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
object.__class__

isinstance(obj, int)
issubclass(bool, int)
class DerivedClassName(Base1, Base2, Base3):

# extend
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update   # private copy of original update() method
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# outside
class Employee:
    pass
john = Employee() # Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# exception
class B:
    pass
class C(B):
    pass
class D(C):
    pass
for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"
#= iterators ================================================
for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char
for line in open("myfile.txt"):
    print line,

s = 'abc'
it = iter(s)
it.next()

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print char

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print char
#= lib ================================================
# os
import os
os.getcwd()      # Return the current working directory
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
dir(os)
help(os)

# glob
import glob
glob.glob('*.py')

# sys
import sys
print sys.argv
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.exit()

# re
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

'tea for too'.replace('too', 'two')

# math
import math
math.cos(math.pi / 4.0)
math.log(1024, 2)

# random
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(xrange(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

# internet
import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print line
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()

#datetime
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368

# timeit performance
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()

# logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
#= import ================================================
