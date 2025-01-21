from sage.all import *


class CVP:
    def __init__(self, B, perform_reduction=True):
        
        self.B = B
        if perform_reduction:
            self.R = self.B.LLL(delta=0.75)
        else:
            self.R = self.B
        self.G = None
        self.L = None
        self.r = None

    def babai(self, t):
        if self.G is None:
            self.G = self.R.gram_schmidt()[0]

        b = t
        for i in reversed(range(self.R.nrows())):
            c = ((b * self.G[i]) / (self.G[i] * self.G[i])).round()
            b -= c * self.R[i]

        self.r = t - b
        return self.r

    def kanan(self, t, q = None):
        if q is None:
            q = t.norm().round()
        
        M = block_matrix([
            [self.B   , Integer(0)],
            [matrix(t), Integer(q)]
        ])
        L = M.LLL()

        for i in range(L.nrows()):
            if L[i][-1] == q:
                break
        else:
            raise ValueError("No solution found")
        
        self.L = L
        
        self.r = t - L[i][:-1]
        return self.r
    

def babai_cvp(B, t, perform_reduction=True):
    return CVP(B, perform_reduction).babai(t)

def kanan_cvp(B, t, q = None):
    return CVP(B).kanan(t, q)

__all__ = ['babai_cvp', 'kanan_cvp', 'CVP']

if __name__ == '__main__':
    B = matrix([
        [  10,  13,  19],
        [  21,  23,  29],
        [   3,   5,   7]
    ])
    t = vector([1, 2, 3])
    print(babai_cvp(B, t))
    print(kanan_cvp(B, t))