# linux pipe style port to python

code like this: `pipe(1) | float | str | list | done` !

[![Build Status](https://travis-ci.org/v2e4lisp/pipeto.png)](https://travis-ci.org/v2e4lisp/pipeto)
tested on 2.7, 3.2, 3.3

## Install
```bash
pip install pipeto
```

## API
* `pipe(arg)`  
generate a pipable object pipe to next function.  
@param : arg {mixed}

* `done(arg)`  
get the actural value out of pipable object

* `compose(fn)`  
Compose functions. Can be used as a decorator.  
@alias : composable  
@param : fn {callable}

* `partial(fn)`  
make a function a partial application. Can be used as a decorator if you like.  
@alias : partialable  
@param : fn {callable}

## example
```python
from pipeto import *
import operation as op

# partial
inc = partial(op.add) | 1
double = partial(op.mul) | 2
mapinc = partial(map) | inc

# pipe
pipe(1) | float | str | list | done    # == ['1', '.', '0']
pipe(2) | inc | done                   # == 3
pipe(2) | inc | double | done          # == 6
pipe([1,2,3]) | mapinc | sum | done    # == 9

# compose
newfn = compose(inc) | double
newfn(2) # == double(inc(2))
```
