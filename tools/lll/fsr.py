from sage.all import *


__all__ = ['FSR', 'small_roots']


class FSR:
    # Find Small Roots
    def __init__(self, f):
        self.f = f
        self.roots = None
        self.L = None
    
    def solve(self, X=None, m=None, t=None, **kwds):
        N = self.f.parent().characteristic()
        f = self.f.change_ring(ZZ)
        x = f.parent().gen()
        d = f.degree()

        if m is None:
            m = 1
        if t is None:
            t = 1
        if X is None:
            X = ceil(N**(1/d))

        g  = [x**j * N**(m-i) * f**i for i in range(m) for j in range(d) ]
        g.extend([x**i * f**m for i in range(t)])

        B = Matrix(ZZ, len(g), d*m + max(d,t) )
        for i in range(B.nrows()):
            for j in range( g[i].degree()+1 ):
                B[i,j] = g[i][j]*X**j

        L = B.LLL(**kwds)
        self.L = L

        f = self.construct_f(X, 0)
        roots = f.roots()

        ZmodN = self.f.base_ring()

        self.roots = roots

        return list(set([ZmodN(r) for r,_ in roots if abs(r) <= X]))
    
    def construct_f(self, X, n, x = None):
        L = self.L
        if x is None:
            x =  PolynomialRing(ZZ, 'x').gen()
        return sum([ZZ(L[n,i]//X**i)*x**i for i in range(L.ncols())])


def small_roots(fn, X=None, m = None, t = None, **kwds):
    return FSR(fn).solve(X, m, t, **kwds)

def test_small_roots():
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    from Crypto.Cipher import AES

    n = 12570456849944679098186723947152758076918489830651403079284169446404625442490910017781070615187402104214216399809182937880611755163051309491883795021742804949023553032332542295660796667242022518314767843250889249103817637908135795592511947286919871996360197931371560500639093524624113768231050393254318350915793997568701268455230769370869415440632905131985229665243329808171142827973341559832544874619902456923738100401024970219160040528452886652320421093118910919399399915983614246095485179031828535146172893244199765707745548669981235169433883496214866262639018924523799592644962862630247577782290343072292165697671
    e = 11
    c = 11276541032586949246844141377353197321010319816579513476202818859950634073869666277625038550186375548836621570493529486729035580032312133662923261378894031844817420780274170506013814020605758923571210820220252262197967425904891849822393845111861753273957697627136801599937302294337365935933213929217485852783472471513318440008982766723273575911073834027327722437695123230969533109931963070248936509928369455318740257419513698206619930772777514093513731577310086099629156506889590500241277813539722604971664784934637880106045996347868822492196822660909331522139833016329546428321518546854640782410360752793170155995966
    enc_flag = 'ebb677500505fdd6a7509a5304c8524216595cd9e08f53727fd733d65d0a7d75'

    a = bytes_to_long(b'\xff' * (2048 // 8 - 16 - 1) + 16*b'\x00')

    x = PolynomialRing(Zmod(n), 'x').gen()
    f = (a + x) ** e - c
    roots = small_roots(f, X=2**128, m=3, t=1, delta=0.75)

    key = roots[0]

    cipher = AES.new(long_to_bytes(int(key)), AES.MODE_ECB)
    print(cipher.decrypt(bytes.fromhex(enc_flag)))


if __name__ == '__main__':
    test_small_roots()