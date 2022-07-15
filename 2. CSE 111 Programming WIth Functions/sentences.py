import random
from random import randint

def main():

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

        word = ''

        word_1 = ["a", "one", "the"]

        word_2 = ["two", "some", "many", "the"]

        if quantity == 1:
            word = word_1[random.randint(0,3)]
        else:
            word = word_2[random.randint(0,4)] 

        return word.capitalize()

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
        noun =''

        noun_1 = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

        noun_2 = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

        if quantity == 1:
            noun = noun_1[random.randint(0, 11)]

        else:
            noun = noun_2[random.randint(0,11)]
        
        return noun

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
        verb = ''

        past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

        present_verbs_1 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

        present_verbs_2 = ["drink","eat" "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
                
        future_verbs = ["will drink", "will eat", "will grow", "wil laugh", "will think", "will sleep", "will talk", "will walk", "will write"]

        if  tense == "past":
            verb = past_verbs[random.randint(0,10)]

        elif quantity == 1 and tense == "present":
            verb = present_verbs_1[random.randint(0,10)]

        elif quantity != 1 and tense == "present":
            verb = present_verbs_2[random.randint(0,10)]

        elif tense == "future":
            verb = future_verbs[random.randint(0,10)]

        return verb

    print(str(get_determiner(1))+' '+str(get_noun(1))+' '+str(get_verb(1, 'past')+'.'))
    print(str(get_determiner(1))+' '+str(get_noun(1))+' '+str(get_verb(1, 'present')+'.'))
    print(str(get_determiner(1))+' '+str(get_noun(1))+' '+str(get_verb(1, 'future')+'.'))
    print(str(get_determiner(2))+' '+str(get_noun(2))+' '+str(get_verb(2, 'past')+'.'))
    print(str(get_determiner(2))+' '+str(get_noun(2))+' '+str(get_verb(2, 'present')+'.'))
    print(str(get_determiner(2))+' '+str(get_noun(2))+' '+str(get_verb(2, 'future')+'.'))

if __name__ == "__main__":
    main()
