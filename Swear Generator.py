#computer insults the guy you hate from 3 choice insults
import random

def insult(name):
    swear = random.choice(['Fuck you', 'Tui ekta madarchod', 'Laura chush'])
    print(swear + ', ' + name)
    z = name
    return z
print('Insert the name of someone you hate: ')
guy_u_hate = input()
x = insult(guy_u_hate)
print('Here we are insulting ' + x)
