import itertools

cxor = lambda a, b: bytes([x ^ y for x, y in zip(a, itertools.cycle(b))])
txor = lambda a, b: bytes([x ^ y for x, y in zip(a, b)])

__all__ = ['cxor', 'txor']