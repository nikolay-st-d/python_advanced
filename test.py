male = 1
female = 1
family = male + female
some_condom = 'Any brand'


def use_condom(condom):
    if condom:
        return True
    return False


if not use_condom(some_condom):
    family = 3
    print('Game Over!')