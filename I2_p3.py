from os.path import join

datos = []
with open('Electricidad.csv')as archivo:
    for line in archivo.readlines():
        datos.append(line.strip().split(','))
datos_necesarios = [datos[4], datos[11]]
info = {}
for pos, dato in enumerate(datos_necesarios[0]):
    info[dato] = datos_necesarios[1][pos]
print(info)
total = 0
for energia in info.keys():
    if energia != '' and energia != 'Units':
        total += int(info[energia])
        print(f"{energia}: {int(info[energia])/(10**6)} {info['Units']}")
print(f"Total: {int(total)/(10**6)} {info['Units']}")
