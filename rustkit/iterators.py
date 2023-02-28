from fishhook import hook
import functools

@hook(object)
def iter(self):
    class Iterator:
        def __init__(self, iterable):
            self.iterable = iterable
        
        def __str__(self):
            return f'Iterator[{type(self.iterable).__name__}]<{self.count()}>'
        
        def Py_Iter(self):
            return dict(__builtins__)['iter'](self.iterable)
        
        def next(self):
            return next(dict(__builtins__)['iter'](self.iterable))
        
        def nth(self, N: int):
            for i in range(N):
                next(dict(__builtins__)['iter'](self.iterable))
        
        def last(self):
            _tmp = [i for i in self.iterable]
            return _tmp[-1]
        
        def count(self):
            _tmp = [i for i in self.iterable]
            return len(_tmp)
        
        def collect(self, container: type):
            _tmp = [i for i in self.iterable]
            return container(_tmp)
        
        def fold(self, func, iterable, initializer=None):
            if initializer is not None:
                return functools.reduce(func, iterable, initializer)
            else:
                return functools.reduce(func, iterable)
        
        @property
        def min(self):
            _tmp = [i for i in self.iterable]
            return min(_tmp)
        
        @property
        def max(self): 
            _tmp = [i for i in self.iterable]
            return max(_tmp)
        
        def position(self, iterable, value):
            try:
                return iterable.index(value)
            except ValueError:
                return -1
        
        def rposition(self, iterable, value):
            try:
                return len(iterable) - iterable[::-1].index(value) - 1
            except ValueError:
                return -1
        
        def any(self, predicate):
            _tmp = [i for i in self.iterable]
            return any(predicate)
        
        def all(self, predicate):
            _tmp = [i for i in self.iterable]
            return all(predicate)
        
        def enumerate(self):
            return enumerate([i for i in self.iterable])
        
        def zip(self, iterator_):
            return zip([i for i in self.iterable], [i for i in iterator_])
        
    return Iterator(self)
