class MyIterable(object):
    def __init__(self, items):
        """items -- List of items."""
        self.items = items

    def __iter__(self):
        return _MyIterator(self)
    
class _MyIterator(object):
    def __init__(self, my_iterable):
        self._my_iterable = my_iterable
        self._position = 0
        
def next(self):
    if self._position >= len(self._my_iterable.items):
        raise StopIteration()
    value = self._my_iterable.items[self._position]
    self._position += 1
    return value

# in Python, iterators also support iter by returning self

def __iter__(self):
    return self
