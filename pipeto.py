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

    - partial(fn)
      use pipe to make a function a partial application. partialable is an
      alias.
      @param: fn {callable}

      e.g.:
      def isum(*args): return sum(args)
      sum6 = partial(sum) | 1 | 2 | 3
      sum6(4) # 10

      mapinc = map | partial(lambda x: x+1)
      # [2,3,4]
      mapinc([1,2,3])
      pipe([1,2,3]) | mapinc | done

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


class _Partial(object):
    def __init__(self, fn):
        self.fn = fn
        self.args = []
        self.kwargs = {}

    def __or__(self, *args, **kwargs):
        self.args.extend(list(args))
        self.kwargs.update(kwargs)
        return self

    def __call__(self, *args, **kwargs):
        args = self.args + list(args)
        kwargs = dict(self.kwargs, **kwargs)
        return self.fn(*args, **kwargs)


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
composalbe = compose


def partial(fn):
    if isinstance(fn, _Partial):
        return fn
    return _Partial(fn)
partialable = partial
