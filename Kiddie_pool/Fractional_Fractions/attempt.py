#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
from fractions import Fraction
import binascii

number1 = int('8905445502561468224327590610508353787915969')
number2 = int('72123363421140648281703145629870876463169591')

flag1 = long_to_bytes(number1)
flag2 = long_to_bytes(number2)
#enc = Fraction(0/1)

#for c in flag:
#    enc += Fraction(int(c)+1)
#    enc = 1/enc
#print(enc)

print (flag1+flag2)

#8905445502561468224327590610508353787915969/72123363421140648281703145629870876463169591