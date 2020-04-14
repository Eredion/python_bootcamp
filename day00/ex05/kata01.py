languages = {
    'Python': 'Guido van Rossum',
    'Ruby' : 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for key in languages:
    print("\033[1;34m{}\033[0;0m was created by {}".format(key, languages[key]))
