# nos caminhos de sys.path

import aula039_m
from aula039_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula039_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula039_m.soma(2, 3))