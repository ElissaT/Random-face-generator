import random
def rand_face():
    eyebrow = ['/', '|', '{', '}']
    eyes = [':', ';', ":'", ";'", ':"', '=']
    nose = ['^', '~', '-', '>']
    mouth = [')', '(', '}', '{', ']', 'o', 'O', 'P', 'p', 'D', 'd']

    fEB = random.choice(eyebrow)
    fE = random.choice(eyes)
    fN = random.choice(nose)
    fM = random.choice(mouth)
    final_face = str(fEB + fE + fN + fM)

    print(''.join(final_face))

rand_face()