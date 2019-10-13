def bottle_of_beer(bob):
    if bob < 1:
        print('no more bottles of beer on the wall.\n'
              'no more bottles of beer.')
        return
    tmp = bob
    bob -= 1
    print('{} bottles of beer on the wall.\n'
          '{} bottle of beer.\n'
          'Take one down, pass it around,\n'
          '{} bottles of beer on the wall.\n'
          .format(tmp, tmp, bob))
    bottle_of_beer(bob)


bottle_of_beer(99)
