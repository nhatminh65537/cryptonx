from sage.all import *


__all__ = ['SSP', 'subset_sum']


class SSP:
    # Subset Sum Problem
    def __init__(self, A = [], s = [], M = None):
        self.A = A
        self.s = s
        self.M = M
        self.B = None
        self.L = None
    
    def solve(self, N = None, **kwds):
        k = len(self.A)
        n = len(self.A[0])
        if N is None:    
            N = ceil(n**(1/2)) if k == 1 else ceil(((n+1)/4)**(1/2))

        I = identity_matrix(n)
        H = ones_matrix(1, n)/2
        A = Matrix(self.A).transpose() * N
        S = Matrix(self.s) * N
        B = [
            [I, Integer(0), A],
            [H, Rational(1/2),S]
        ]
        
        if self.M is not None:
            M = identity_matrix(k)*self.M*N
            B.insert(1, [Integer(0), Integer(0), M])
        B = block_matrix(B)
        
        L = B.LLL(**kwds)
        for v in L:
            if all(x in [-1/2, 1/2, 0] for x in v):
                break
        if v[n] > 0:
            res = [1 if x == -1/2 else 0 for x in v[:n]]
        else:
            res = [1 if x ==  1/2 else 0 for x in v[:n]]

        self.B = B
        self.L = L

        return res

    def desity(self):
        k = len(self.A)
        n = len(self.A[0])
        if self.M is None:
            b = log(max(map(max, self.A)), 2).n()
        else:
            b = log(self.M, 2).n()
        return n/(k*b)
    
    def min_k(self):
        n = len(self.A[0])
        return n/(log((n + 1)*n**(1/2) + 1, 2)).n()

    def append(self, a, s):
        self.A.append(a)
        self.s.append(s)
        return self


def subset_sum(weights, targets, modulus=None, N=None):
    return SSP(weights, targets, modulus).solve(N)

def test_subset_sum():
    ssp = SSP()
    ssp.append([83,59,47,81,76,51], 291)
    print(ssp.solve(3))
    print(ssp.desity())
    print(ssp.min_k())


if __name__ == '__main__':
    test_subset_sum()