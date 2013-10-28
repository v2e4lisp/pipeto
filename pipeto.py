"""
Command line pipe style port to python

author: wenjun.yan
email : mylastnameisyan@gmail.com

API:
    - pipe(arg)
      pipe the argument to functions. pipe to `done` to get the result
      @param: arg {mixed}

      e.g. :
      pipe(1) | str | list | done # ['1']

    - done(arg)
      `done` is the end of a pipe.  Get result out of Pipe object.

    - compose(fn)
      use pipe to compose functions. `composalbe` is an alias of `compose`,
      in case you may want to use it as a decorator `composable` seems make
      more sense.
      @param: fn {callable}

      e.g. :
      chars = compose(str) | list
      chars(123) # ["1", "2", "3"]

      @composable
      def tostr(x):
          return str(x)
      chars = tostr | list
"""

class _Compose(object):
    def __init__(self, fn):
        self.fns = [fn]

    def __or__(self, fn):
        if isinstance(fn, _Compose):
            self.fns.extend(fn.fns)
        else:
            self.fns.append(fn)
        return self

    def __call__(self, *args, **kwargs):
        init = self.fns[0](*args, **kwargs)
        for f in self.fns[1:]:
            init = f(init)
        return init

class _Pipe(object):
    def __init__(self, val):
        self.val = val

    def __or__(self, fn):
        if fn == done:
            return self.val
        self.val = fn(self.val)
        return self


def pipe(arg):
    return _Pipe(arg)


def done(arg):
    return arg


def compose(fn):
    if isinstance(fn, _Compose):
        return fn
    return _Compose(fn)
composable = compose
