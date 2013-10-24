# linux pipe style port to python

[![Build Status](https://travis-ci.org/v2e4lisp/pipeto.png)](https://travis-ci.org/v2e4lisp/pipeto)
tested on 2.7, 3.2, 3.3

## Install
```bash
pip install pipeto
```

## API
* `pipe(arg)`   
generate a pipable object   
@param : arg {mixed}

* `done(*args, **kwargs)`  
get the actural value out of pipable object

* `to(fn)`  
pass the args before to function `fn`and get the return value. The difference between `pipe` and `to` : 
The general pattern for `pipe` is `pipe(arg) | fn1 | fn2 | fn3 | done`.  
And for `to` is `arg | to(fn1) | to(fn2) | to(fn3)`. (No `done` is need here!)  
@param : fn {function}

* `compose(fn)`
compose functions.  
@param : fn {function}

## example
```python
from pipeto import *

def add1(x): return x + 1

def minus(x): return 0 - x

def double(x): return x * 2

 2 | to(add1) | to(double) | to(minus) # == minus(double(add1(2)))
 pipe(2) | add1 | done # == add1(2)
 pipe(2) | add1 | double | minus | done # == minus(double(add1(2)))
 (compose(add1) | double | minus)(2) # == minus(double(add1(2)))
 pipe(3) | add1 | minus | double | done # == double(minus(add1(3)))
```
