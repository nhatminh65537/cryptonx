from sage.all import *


__all__ = ['HNP', 'hnp_by_cvp', 'hnp_by_svp']


class HNP:
    # Hidden Number Problem
    def __init__(self, p, a = [], t = []):
        assert len(a) == len(t), "a and t must have the same length"
        self.p = p
        self.a = a
        self.t = t
        self.M = None
        self.E = None
        self.L = None
        self.cvp = None
    
    def solve_by_cvp(self, B = None):
        from .cvp import CVP

        if B is None:
            B = self.p
        m = len(self.a)
        a = vector(self.a + [0])
        p = self.p
        
        M = block_matrix([
            [identity_matrix(m)*p, Integer(0)],
            [matrix(self.t), Rational(1/p)]
        ])

        self.cvp = CVP(M)
        x = self.cvp.babai(a)

        self.M = M
        
        r = (x - a)[-1]*p % p 
        return r
    
    def solve_by_svp(self, B = None, **kwds):
        if B is None:
            B = self.p
        m = len(self.a)
        p = self.p
        
        E = block_matrix([
            [identity_matrix(m)*p, Integer(0), Integer(0)],
            [matrix(self.t), Rational(B/p), Integer(0)],
            [matrix(self.a), Integer(0), Integer(B)]
        ])
        L = E.LLL(**kwds)

        for v in L:
            if all(abs(x) <= B for x in v[:m]) and abs(v[-1]) == B:
                break
                
        self.E = E
        self.L = L

        s = -1 if -v[-1]/B < 0 else 1
        return v[m]*p/B*s % p
    
    def append(self, a, t):
        self.a.append(a)
        self.t.append(t)
        return self
    
    def bound(self):
        p = self.p
        k = round(sqrt(log(p, 2))) + round(log(log(p, 2), 2))
        return n(p/2**k)

    def min_m(self):
        p = self.p
        return n(2*round(sqrt(log(p, 2))))


def hnp_by_cvp(p, a, t, B = None):
    return HNP(p, a, t).solve_by_cvp(B)

def hnp_by_svp(p, a, t, B = None, **args):
    return HNP(p, a, t).solve_by_svp(B, **args)

def test_hnp():
    p = 401
    hnp = HNP(p, [62, 300, 86], [143, 293, 304])
    print(hnp.solve_by_cvp(20))
    print(hnp.solve_by_svp(20))
    print(hnp.bound())
    print(hnp.min_m())


if __name__ == '__main__':
    test_hnp()