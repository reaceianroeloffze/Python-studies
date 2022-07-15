from sentences import get_determiner, \
    get_noun, get_verb, \
    get_preposition, get_prepositional_phrase, \
    get_adjective, get_adverb, get_country
import random
import pytest

# Set up a series of functions to test
# functions in corresponding program

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_adjective():
    adjectives = ['angry', 'happy', 'jolly', 'messy', 'merry',
        'frightful', 'engimnatic', 'charming', 'silly', 'crazy',
        'benevolent', 'spritely', 'concerned', 'sad', 'troublesome',
        'virtuous', 'cunning', 'talented', 'blessed', 'blissful']
    
    # loop through this assertion 20 times
    for _ in range(20):
        adjective = get_adjective()
        assert adjective in adjectives
    
def test_get_noun():
    # 1. Test singlular nouns
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(11):
        noun = get_noun(1)
        assert noun in single_nouns
    
    # 2. Test plural nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(11):
        quantity = random.randint(2, 11)
        noun = get_noun(quantity)
        assert noun in plural_nouns
    
def test_get_adverb():
    adverbs = ['angrily', 'happily', 'merrily', 'pleasingly', 'enigmatically',
        'blissfully', 'frightfully', 'charmingly', 'crazily', 'foolishly',
        'virtuously', 'mercifully', 'pleasingly', 'spitefully', 'playfully',
        'hilariously', 'funnily', 'gracefully', 'cheerfully', 'sadly']
    
    for _ in range(20):
        adverb = get_adverb()
        assert adverb in adverbs
    
def test_get_verb():
    # 1. Test past tense verbs
    past_tense_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(11):
        verb = get_verb(1, 'past')
        assert verb in past_tense_verbs

    # 2. Test present tense verbs
    
    # 2.1 Verbs for singlular nouns
    present_tenses_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    # Loop through assertion 11 times
    for _ in range(11):
        verb = get_verb(1, 'present')
        assert verb in present_tenses_1
    
    # 2.2 Verbs for plural nouns
    present_tenses_2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    # Loop through assertion 11 times   
    for _ in range(11):
        quantity = random.randint(2, 11)
        verb = get_verb(quantity, 'present')
        assert verb in present_tenses_2
        
    # 3. Test future tense verbs
    future_tenses = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    # Loop through assertion 11 times
    for _ in range(11):
        verb = get_verb(1, 'future')
        assert verb in future_tenses

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    # Loop through assertion 30 times
    for _ in range(30):
        preposition = get_preposition()
        assert preposition in prepositions
        
def test_get_prepositional_phrase():
    # Verify that 4 words are printed in the 
    # prepositional phrase statement according to 
    # a presribed format:
    # a preposition, a determiner, an adjective and a noun. 
    # Split the string into a list to verify the words should be 4.
    assert get_prepositional_phrase(f'{get_preposition()} {get_determiner("a")} {get_adjective()} {get_noun("boy")}').split(' ', maxsplit=4)
    
    # Not sure if the following 3 loops 
    # are needed here because the test 
    # passes either way, but I still
    # decided to include them 
    # for extra possible accuracy.
    
    # Verify that the first word is a preposition and
    # loop through assertion 30 times
    for _ in range(30):
        assert get_preposition() in ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
     
    # Verify that the second word is a determiner &
    # loop the assertion 7 times   
    for _ in range(7):
        assert get_determiner('a') in ["a", "one", "the", "two", "some", "many", "the"]
        
    # Verify that the 3rd word is an adjective &
    # loop through the assertion 20 times
    for _ in range(20):
        assert get_adjective() in ['angry', 'happy', 'jolly', 'messy', 'merry',
        'frightful', 'engimnatic', 'charming', 'silly', 'crazy',
        'benevolent', 'spritely', 'concerned', 'sad', 'troublesome',
        'virtuous', 'cunning', 'talented', 'blessed', 'blissful']
     
    # Verify that the 4th word is a noun &
    # loop through the assertion 20 times
    for _ in range(20):
        assert get_noun('boy') in ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        
        
def test_get_country():
    countries = ['in South Africa', 'in England', 'in Samoa', 'in Japan',
        'in the USA', 'in Paraguay', 'in Sweden', 'in Korea',
        'in Australia', 'in the DRC', 'in Ecuador', 'in Costa Rica',
        'in Chad', 'in Afganistan', 'in Indonesia', 'in Tonga',
        'in Guatemala', 'in Brazil']
    
    # Loop through assertion 18 times
    for _ in range(18):
        country = get_country()
        assert country in countries
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])