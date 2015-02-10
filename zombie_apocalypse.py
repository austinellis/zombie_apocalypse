from zombie_class import ZombieApoc

zombie = ZombieApoc()

print 'Welcome to the Zombie Apocalypse Simulator'
# print 'First we\'ll ask some questions about your zombies. \n'
#custom_pop = raw_input('The world\'s current population is 7,276,206,460. Would you like to change this? (Y or N)' )


def print_menu():
    print 'Menu:'
    print '1) Change population'
    print '2) Change Immunite Percentage'
    print '3) Change number of humans each zombie infects per day'
    print '4) Run simulation'
    print '5) Help'


def menu_input():
    action = raw_input('What would you like to do? ')

    if action == '1':
        population = raw_input('The current population is 7,276,206,460. ' \
            'What is your world\'s population? ')
        zombie.ChangePop(population)

    elif action == '2':
        print zombie.population
        population = raw_input('What is your world\'s population? ')
        zombie.ChangePop(population)
        print zombie.population

    elif action == '3':
        pass

    elif action == '4':
        pass

    elif action == '5':
        pass

print_menu()
menu_input()
