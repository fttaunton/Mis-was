from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate

P = 'P'
Q = 'Q'
T = 'T'
S = 'S'
H = 'H'
fluidos = ['water', 'ammonia', 'R134A']
eficiencia = {}
trabajo_neto = {}
for fluido in fluidos:
    p = {}
    t = {}
    h = {}
    s = {}
    q = {}
    p[2] = 0.4761 * (10**6)  # Se puede variar perro
    q[6] = 0.85
    q[1] = 0
    t[1] = 40 + 273.15
    p[1] = prop('P', 'T', t[1], 'Q', q[1], fluido)
    t[3] = 150 + 273.15
    t[5] = t[3]
    s[1] = prop('S', 'T', t[1], 'Q', q[1], fluido)
    h[1] = prop('H', 'T', t[1], 'Q', q[1], fluido)
    s[2] = s[1]
    p[3] = p[2]
    s[3] = prop('S', 'T', t[3], P, p[3], fluido)
    s[4] = s[3]
    p[6] = p[1]
    t[6] = t[1]
    s[6] = prop('S', 'T', t[6], 'Q', q[6], fluido)
    h[6] = prop('H', 'T', t[6], 'Q', q[6], fluido)
    s[5] = s[6]
    p[5] = prop('P', 'T', t[5], 'S', s[5], fluido)
    p[4] = p[5]
    t[2] = prop('T', 'S', s[2], 'P', p[2], fluido)
    t[4] = prop('T', 'S', s[4], 'P', p[4], fluido)
    q[4] = prop('Q', 'T', t[4], 'S', s[4], fluido)
    if q[4] >= 0 and q[4] <= 1:
        h[4] = prop('H', 'T', t[4], 'Q', q[4], fluido)

    for i in range(6):
        if i+1 not in s.keys():
            print(i+1)
            s[i+1] = prop('S', 'H', h[i+1], 'P', p[i+1], fluido)
        if i+1 not in h.keys():
            print(i+1)
            h[i+1] = prop('H', 'T', t[i+1], 'P', p[i+1], fluido)
    lista = [['Punto', 't [°C]', 'p [Pa]',  's [J/kgK]', 'h [J/kg]']]
    for i in range(1, 7):
        lista.append([i, t[i]-273.15, p[i], s[i], h[i]])
    print('\n')
    print(fluido.upper())
    print(tabulate(lista))
    trabajo_neto[fluido] = (0.9*(h[3] - h[4] + h[5]- h[6])- h[2] + h[1])
    eficiencia[fluido] = (0.9*(h[3] - h[4] + h[5]- h[6])- h[2] + h[1])/(h[3] - h[2] + h[5] -h[4])
    print(f'Eficiencia: {eficiencia[fluido]*100}%, Trabajo neto: {trabajo_neto[fluido]} kJ/kg')
    print('\n')
print(trabajo_neto)
print(eficiencia)