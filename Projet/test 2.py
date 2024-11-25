print('1.Commencez votre aventure !\n2.Explication du Jeu\n3.Quittez le jeu')
option = input('Entrer votre choix:')

if option == '1':
    start_game()
elif option == '2':
    help_menu()
elif option == '3':
    sys.exit()
while option not in ['1', '2', '3']:
    print('1.Commencez votre aventure !\n2.Explication du Jeu\n3.Quittez le jeu')
    if option == '1':
        start_game()
    elif option == '2':
        help_menu()
    elif option == '3':
        sys.exit()
