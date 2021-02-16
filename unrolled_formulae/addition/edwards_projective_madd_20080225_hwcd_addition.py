from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('c', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
c, d, X1, X2, Y1, Y2 = pr.gens()
ccd = c * c * d
ccd2 = 2 * c * c * d
c2 = 2 * c
cc4 = 4 * c * c
k = 1 / c
Z1, Z2 = 1, 1
formula = {}
A = X1
formula['A'] = A
B = Y1
formula['B'] = B
C = Z1 * X2
formula['C'] = C
D = Z1 * Y2
formula['D'] = D
E = A * B
formula['E'] = E
F = C * D
formula['F'] = F
G = E + F
formula['G'] = G
H = E - F
formula['H'] = H
t0 = A - C
formula['t0'] = t0
t1 = B + D
formula['t1'] = t1
t2 = t0 * t1
formula['t2'] = t2
J = t2 - H
formula['J'] = J
t3 = A + D
formula['t3'] = t3
t4 = B + C
formula['t4'] = t4
t5 = t3 * t4
formula['t5'] = t5
K = t5 - G
formula['K'] = K
X3 = G * J
formula['X3'] = X3
Y3 = H * K
formula['Y3'] = Y3
t6 = J * K
formula['t6'] = t6
Z3 = k * t6
formula['Z3'] = Z3
