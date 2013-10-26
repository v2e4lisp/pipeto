"""
Command line pipe style port to python

author: wenjun.yan
email : mylastnameisyan@gmail.com

API:
    - pipe(fn)
      pipe arguments to functions. pipe to `done` to get the result
      @param: fn {callable}

      e.g. :
      pipe(1) | str | list | done # ['1']

    - done(arg)
      `done` is the end of a pipe.  Get result out of Pipe object.

    - to(fn)
      yet another way to pipe args to functions. no need to pipe to `done`
      @param: fn {callable}

      e.g. :
      1 | to(str) | to(list) # ['1']

    - compose(fn)
      use pipe to compose functions
      @param: fn {callable}

      e.g. :
      chars = compose(str) | list
      chars(123) # ["1", "2", "3"]

    - partial(fn)
      use pipe to make a function a partial application.
      @param: fn {callable}

      e.g.:
      def isum(*args): return sum(arg)
      sum6 = isum | partial(1) | partial(2) | partial(3)
      sum6(4) # 10

      mapinc = map | partial(lambda x: x+1)
      mapinc([1,2,3]) # [2,3,4]

"""

class _Compose(object):
    def __init__(self, fn):
        self.fns = [fn]

    def __or__(self, fn):
        self.fns.append(fn)
        return self

    def __call__(self, *args, **kwargs):
        init = self.fns[0](*args, **kwargs)
        for f in self.fns[1:]:
            init = f(init)
        return init


class _Partial(object):
    def __init__(self, *args, **kwargs):
        self.fn = None
        self.args = list(args)
        self.kwargs = kwargs

    def __ror__(self, fn):
        self.fn = fn
        return self

    def __or__(self, part):
        self.args.extend(part.args)
        self.kwargs.update(part.kwargs)
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


class _To(object):
    def __init__(self, fn):
        self.fn = fn

    def __ror__(self, arg):
        return self.fn(arg)

    def __call__(self, arg):
        return self.fn(arg)


def pipe(arg):
    if isinstance(arg, _Pipe):
        return arg
    return _Pipe(arg)


def done(arg):
    return arg


def to(fn):
    if isinstance(fn, _To):
        return fn
    return _To(fn)
pipable = to


def compose(fn):
    if isinstance(fn, _Compose):
        return fn
    return _Compose(fn)
composalbe = compose


def partial(*args, **kwargs):
    return _Partial(*args, **kwargs)

