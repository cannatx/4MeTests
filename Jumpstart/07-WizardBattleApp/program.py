# import actors
from actors import Creature, Wizard


def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------------------')
    print('------------ Battle Wizard --------------')
    print('-----------------------------------------')
    print('')


def game_loop():
    creatures = [
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature(),
    ]

    hero = Wizard()

    while True:

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if cmd == 'a':
            print('attack ')
        elif cmd == 'r':
            print('runaway ')
        elif cmd == 'l':
            print('Look Around ')
        else:
            print('OK, exiting the Game.... bye!')
            break


if __name__ == '__main__':
    main()
