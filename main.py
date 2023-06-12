from random import choice, randint


def main():

    nouns = getwords('nouns.txt')
    verbs = getwords('verbs.txt')
    for i in range(len(verbs)):
        verbs[i] = verbs[i].split(',')
    adjectives = getwords('adjectives.txt')
    prepositions = getwords('prepositions.txt')
    for j in range(5):
        print(createsentence(nouns, verbs, adjectives, prepositions))


def getwords(source):
    file = open(source, 'r')
    returnvalue = file.read()
    file.close()
    return returnvalue.split('\n')


def createsentence(nounlist, verblist, adjectivelist, prepositionlist):
    sentence = ''
    word = choice(nounlist)
    word = article(word)
    sentence += word + ' '

    word = formtimeform(choice(verblist))
    sentence += word

    sentence += ' ' + prepositionlist[randint(0, len(prepositionlist)-1)] + ' '
    word = choice(nounlist)
    word = article(word)
    sentence += word + '.'
    sentence = sentence.upper()[:1] + sentence[1:]
    return sentence


def article(unarticled):
    vocals = ['a', 'e', 'i', 'o', 'u']

    if unarticled[0] in vocals:
        unarticled = 'an ' + unarticled
    elif unarticled[0] not in vocals:
        unarticled = 'a ' + unarticled
    return unarticled


def formtimeform(sublist):
    timeform = randint(0, len(sublist)-1)
    verb = sublist[timeform]
    if timeform == 0:
        return verb + 's'
    elif timeform == 1:
        return verb
    elif timeform == 2:
        return 'had ' + verb


if __name__ == '__main__':
    main()