import importlib

import aula040_m

print(aula040_m.variavel)

for i in range(10):
    importlib.reload(aula040_m)
    print(i)

print('Fim')