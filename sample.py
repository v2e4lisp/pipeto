import operator as op
from pipeto import *

inc = op.add | partial(1)
double = op.mul | partial(2)
incdouble = pipable(compose(inc) | double)

print 10 | incdouble

print pipe(1) | double | inc | double | inc | done
print pipe(1) | inc | inc | inc | double | done

def add1(x): return x + 1

def minus(x): return 0 - x

def double(x): return x * 2

print 2 | to(add1) | to(double) | to(minus)
print pipe(2) | add1 | done
print pipe(2) | add1 | double | minus | done
print (compose(add1) | double | minus)(2)

print pipe(3) | add1 | minus | double | done
