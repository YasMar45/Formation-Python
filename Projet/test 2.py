print('1.Commencez votre aventure !\n2.Quittez le jeu')
option = input('Entrer votre choix:')

if option == '1':
    start_game()
if option == '2':
    sys.exit()
while option not in ['1', '2']:
    print('1.Commencez votre aventure !\n2.Quittez le jeu')
    option = input('Entrer votre choix:')
    if option == '1':
            start_game()
    if option == '2':
            sys.exit()