import random

# Define the main function
def main():
    
    # Print and call functions for singular sentences
    print (f'\033[31;1m{get_determiner(1).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(1)} \033[32;1m{get_prepositional_phrase(1)} \033[34;1m{get_adverb()} \033[36;1m{get_verb(1, "past")} \033[32;1m{get_prepositional_phrase(1)} \033[30;1m{get_country()}\033[0m.')
    print (f'\033[31;1m{get_determiner(1).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(1)} \033[32;1m{get_prepositional_phrase(1)} \033[34;1m{get_adverb()} \033[36;1m{get_verb(1, "present")} \033[32;1m{get_prepositional_phrase(1)} \033[30;1m{get_country()}\033[0m.')
    print (f'\033[31;1m{get_determiner(1).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(1)} \033[32;1m{get_prepositional_phrase(1)} \033[36;1m{get_verb(1, "future")} \033[32;1m{get_prepositional_phrase(1)} \033[30;1m{get_country()}\033[0m.')
    
    # print and call functions for plural sentences
    print (f'\033[31;1m{get_determiner(2).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(2)} \033[32;1m{get_prepositional_phrase(2)} \033[34;1m{get_adverb()} \033[36;1m{get_verb(2, "past")} \033[32;1m{get_prepositional_phrase(2)} \033[30;1m{get_country()}\033[0m.')
    print (f'\033[31;1m{get_determiner(2).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(2)} \033[32;1m{get_prepositional_phrase(2)} \033[34;1m{get_adverb()} \033[36;1m{get_verb(2, "present")} \033[32;1m{get_prepositional_phrase(2)} \033[30;1m{get_country()}\033[0m.')
    print (f'\033[31;1m{get_determiner(2).capitalize()} \033[33;1m{get_adjective()} \033[35;1m{get_noun(2)} \033[32;1m{get_prepositional_phrase(2)} \033[36;1m{get_verb(2, "future")} \033[32;1m{get_prepositional_phrase(2)} \033[30;1m{get_country()}\033[0m.')

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_adjective():
    '''Return a randomly chosen adjective from
    the following list of adjectives:
        'angry', 'happy', 'jolly', 'messy', 'merry',
        'frightful', 'engimnatic', 'charming', 'silly', 'crazy',
        'benevolent', 'spritely', 'concerned', 'sad', 'troublesome',
        'virtuous', 'cunning', 'talented', 'blessed', 'blissful'
    '''
    adjectives = ['angry', 'happy', 'jolly', 'messy', 'merry',
        'frightful', 'engimnatic', 'charming', 'silly', 'crazy',
        'benevolent', 'spritely', 'concerned', 'sad', 'troublesome',
        'virtuous', 'cunning', 'talented', 'blessed', 'blissful']
    
    # Randomly choose and return an adjective
    adjective = random.choice(adjectives)
    return adjective

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # randomly choose and return a noun
    noun = random.choice(nouns)
    return noun

def get_adverb():
    '''Return a randomly chosen adverb
    for the past and present tense 
    from the following list:
        'angrily', 'happily', 'merrily', 'pleasingly', 'enigmatically',
        'blissfully', 'frightfully', 'charmingly', 'crazily', 'foolishly',
        'virtuously', 'mercifully', 'pleasingly', 'spitefully', 'playfully',
        'hilariously', 'funnily', 'gracefully', 'cheerfully', 'sadly'
    '''
    adverbs = ['angrily', 'happily', 'merrily', 'pleasingly', 'enigmatically',
    'blissfully', 'frightfully', 'charmingly', 'crazily', 'foolishly',
    'virtuously', 'mercifully', 'pleasingly', 'spitefully', 'playfully',
    'hilariously', 'funnily', 'gracefully', 'cheerfully', 'sadly']
    
    # Return a randomly chosen adverb
    adverb = random.choice(adverbs)
    return adverb

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote",
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes",
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write",
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense == 'present' and quantity == 1:
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    if tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    # randomly choose and return a verb
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a preposition
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    # Return a prepositional phrase in a designated format
    prepositional_phrase = f'{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}'
    return prepositional_phrase

def get_country():
    '''Return a randomly selected country
    from this list:
        'in South Africa', 'in England', 'in Samoa', 'in Japan',
        'in the USA', 'in Paraguay', 'in Sweden', 'in Korea',
        'in Australia', 'in the DRC', 'in Ecuador', 'in Costa Rica',
        'in Chad', 'in Afganistan', 'in Indonesia', 'in Tonga',
        'in Guatemala', 'in Brazil'
    '''
    
    countries = ['in South Africa', 'in England', 'in Samoa', 'in Japan',
        'in the USA', 'in Paraguay', 'in Sweden', 'in Korea',
        'in Australia', 'in the DRC', 'in Ecuador', 'in Costa Rica',
        'in Chad', 'in Afganistan', 'in Indonesia', 'in Tonga',
        'in Guatemala', 'in Brazil']
    
    # Return a randomly selected country
    country = random.choice(countries)
    return country
    
# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()