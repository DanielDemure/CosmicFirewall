# Starter skeleton: toy calculations for Route A
# This script computes the Margolus-Levitin bound and Bekenstein bound
# for given R (m) and E (J) and prints the ops/sec per bit estimate.

import math

hbar = 1.054571817e-34
ln2 = math.log(2)
pi = math.pi

def margolus_levitin_ops(E):
    return 2*E/(pi*hbar)

def bekenstein_bits(R, E):
    # S_max <= 2*pi*k_B*R*E/(hbar*c) ; convert to bits: S/kB/ln2
    c = 299792458.0
    return (2*pi*R*E)/(hbar*c*ln2)

if __name__ == '__main__':
    R = 1.0  # meter
    E = 1e2  # joules
    ops = margolus_levitin_ops(E)
    bits = bekenstein_bits(R, E)
    print('ops/sec (ML bound):', ops)
    print('max bits (Bekenstein):', bits)
    print('ops per bit per sec (estimate):', ops/bits if bits>0 else float('inf'))
