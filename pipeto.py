class _Composer(object):
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
    return _Pipe(arg)

def to(fn):
    return _To(fn)

def compose(fn):
    return _Composer(fn)

def done(*arg, **kwargs): pass
