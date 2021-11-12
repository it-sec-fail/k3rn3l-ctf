from Crypto.Util.number import bytes_to_long
flag = str(bytes_to_long(open('flag.txt','rb').read()))
from fractions import Fraction
enc = Fraction(0/1)
for c in flag:
    enc += Fraction(int(c)+1)
    enc = 1/enc
print(enc)
#8905445502561468224327590610508353787915969/72123363421140648281703145629870876463169591