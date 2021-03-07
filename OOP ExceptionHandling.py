# This line tells the interpreter to only import the content of __all__
# while 'from <module> import *'.  Mainly used when we don't want
# other PGMs to automatically import some of this file's classes/methods.
# If we want to explicitely use, lets say XYZ, from this file, it could
# be done by wether explicit call: 'storage.XYZ' or explicit import
# 'from storage import XYZ'.

__all__ = ['Storage']

class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.

        >>> o = Storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        None

    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return None

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

    def __getstate__(self):
        return dict(self)

    def __setstate__(self, value):
        for k, v in value.items(): self[k] = v