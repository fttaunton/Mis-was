from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate


fluido = 'water'
p = {}
t = {}
h = {}
s = {}
p[3] = 1.5 * (10**6)
t[3] = 280 + 273.15
p[4] = 0.2 * (10**6)
p[5] = 0.1 * (10**6)
t[5] = 60 + 273.15
p[7] = 0.01 * (10**6)
p[1] = p[7]
t[1] = prop('T', 'P', p[1], 'Q', 0, fluido)
p[6] = p[7]
p[2] = p[3]
s[3] = prop('S', 'P', p[3], 'T', t[3], fluido)
t[4] = prop('T', 'S', s[3], 'P', p[4], fluido)
h[5] = prop('H', 'T', t[5], 'P', p[5], fluido)
h[4] = prop('H', 'S', s[3], 'P', p[4], fluido)
s[1] = prop('S', 'P', p[1], 'Q', 0, fluido)
h[1] = prop('H', 'P', p[1], 'Q', 0, fluido)
h[6] = h[5]
s[2] = s[1]
s[7] = s[3]
s[4] = s[3]
t[2] = prop('T', 'S', s[2], 'P', p[2], fluido)
t[6] = t[1]
t[7] = t[1]
h[7] = prop('H', 'S', s[7], 'P', p[7], fluido)
for i in range(7):
    if i+1 not in s.keys():
        if i == 5:
            s[i+1] = prop('S', 'H', h[i+1], 'P', p[i+1], fluido)
        elif i != 3:
            s[i+1] = prop('S', 'T', t[i+1], 'P', p[i+1], fluido)
    if i+1 not in h.keys():
        h[i+1] = prop('H', 'T', t[i+1], 'P', p[i+1], fluido)
lista = [['Punto', 't [°C]', 'p [Pa]',  's [J/kgK]', 'h [J/kg]']]
for i in range(1, 8):
    lista.append([i, t[i]-273.15, p[i], s[i], h[i]])
print('\n')
print(tabulate(lista))
print('\n')
s2 = {}
rango = list(range(374))
printeable1 = []
printeable2 = []
for j in rango:
    printeable1.append(prop('S', 'T', j + 273.15, 'Q', 0, fluido))
    printeable2.append(prop('S', 'T', j + 273.15, 'Q', 1, fluido))
lista_eses = [s[i + 1] for i in range(7)]

lista_tes = [t[i + 1] - 273.15 for i in range(7)]
plot.figure()
plot.plot(printeable2, rango)
plot.plot(printeable1, rango)
plot.plot(lista_eses, lista_tes, 'ro')
plot.ylabel('Temperatura °C')
plot.xlabel('S')
plot.tight_layout()
plot.show()