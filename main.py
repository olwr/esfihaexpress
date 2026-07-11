import classes.Menu as Menu

def print_welcome():
    print('Bem-vindo(a) a Esfiha Express!\n')

if __name__ == '__main__':
    print_welcome()
    menu = Menu.Menu()

    try:
        menu.loop_menu()
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário. Até logo!')
    except EOFError:
        print('\nEntrada encerrada. Até logo!')