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
generate a pipable object  
@param : arg {mixed}

* `done(*args, **kwargs)`
get the actural value out of pipable object

* `compose(fn)`  
compose functions.  
@param : fn {callable}

* `partial(fn)`  
make a function a partial application.  
@param : fn {callable}

## example
```python
from pipeto import *
import operation as op

# partial
inc = partial(op.add) | 1
double = partial(op.mul) | 2

# pipe
pipe(1) | float | str | list | done    # == ['1', '.', '0']
pipe(2) | inc | done                   # == inc(2)
pipe(2) | inc | double | done          # == double(inc(2))

# compose
newfn = compose(inc) | double
newfn(2) # == double(inc(2))
```
