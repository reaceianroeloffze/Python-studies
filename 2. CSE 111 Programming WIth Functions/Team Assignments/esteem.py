import math

NEGATIVE = -1
POSITIVE = 1

# define main function
def main():
    
    # print introductory text
    print (f'This program is an implementation of the Rosenberg \n'
            'Self-Esteem Scale. This program will show you ten \n'
            'statements that you could possibly apply to yourself \n'
            'Please rate how much you agree with each of the \n'
            'statements by responding with one of these four letters \n\n'
            'D means you strongly disagree with the statement \n'
            'd means you disagree with the statement \n'
            'a means you agree with the statement \n'
            'A means you strongly agree with the statement.\n')
    
    
    score = 0
    score += get_answer('1. I feel that I am a person of worth, at least on an equal plane with others.', POSITIVE)
    score += get_answer('2. I feel that I have a number of good qualities.', POSITIVE)
    score += get_answer('3. All in all, I am inclined to feel that I am a failure.', NEGATIVE)
    score += get_answer('4. I am able to do things as well as most other people.', POSITIVE)
    score += get_answer('5. I feel I do not have much to be proud of.', NEGATIVE)
    score += get_answer('6. I take a positive attitude toward myself.', POSITIVE)
    score += get_answer('7. On the whole, I am satisfied with myself.', POSITIVE)
    score += get_answer('8. I wish I could have more respect for myself.', NEGATIVE)
    score += get_answer('9. I certainly feel useless at times.', NEGATIVE)
    score += get_answer('10. At times I think I am no good at all.', NEGATIVE)
    
    print (f'Your score is: {score}\n'
            'A score below 15 indicates problematic low self-esteem')
    
def get_answer(statement, positive_or_negative):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    
    print (statement)
    value = input("Enter D, d, a, or A: ")
    score = 0
    if value == 'D':
        score = 0
    elif value == 'd':
        score = 1
    elif value == 'a':
        score = 2
    elif value == 'A':
        score = 3
        
    if positive_or_negative == NEGATIVE:
        score = 3 - score
        
    return score

# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()