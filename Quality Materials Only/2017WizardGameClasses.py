import random

from WGActors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------------')
    print('        Wizard Game')
    print('----------------------------')
    print('')


def game_loop():
    creatures = [Creature('toad', 1),
                 Creature('tiger', 12),
                 Creature('bat', 3),
                 Creature('dragon', 50),
                 Creature('evil wizard', 100),
                 ]
    print(creatures)
    hero = Wizard('bill', 75)

    while True:
        active_creature = random.choice(creatures)
        print ('a {} appears!'.format(active_creature))
        cmd = input('Do you [a]ttack , [r]un away or [l]ook around?:   ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Game Over')
                break
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('the wizard sees:')
            for c in creatures:
                print ('* A {} of level {}'.format(c.name, c.level))
        else:
            print('ok, exiting game')
            break


if __name__ == '__main__':
    main()
