import caesar as cs
import multiplicative as mp
import affine as af
import autokey as ak

alpha = ' abcdefghijklmnopqrstuvwxyz'
choose = input()

if choose == '1':
    cs.caesar(alpha)
if choose == '2':
    mp.multipl(alpha)
if choose == '3':
    af.affine(alpha)
if choose == '4':
    ak.autokey(alpha)
