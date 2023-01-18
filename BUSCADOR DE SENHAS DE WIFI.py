import os
os.system('title DEV-CUTE / BUSCADOR DE SENHAS DE WIFI')
os.system('color f0')
perg = 1
while perg == 1:
    os.system('cls')
    print('===========================================')
    print('\tBUSCADOR DE SENHAS DE WIFI')

    print('MENU')
    print('1 - ver perfis \t 2 - ver dados dos Perfis')
    opsao = int(input('\n Escolha uma opsão: '))

    os.system('cls')

    if opsao == 1:
        perfil = os.system(f'netsh wlan show profiles key=clear')
    else:
        valor = input('Informe o nome do perfil para ver os dados: ')
        perfil = os.system(f'netsh wlan show profile "{valor}" key=clear')
        
    input()
