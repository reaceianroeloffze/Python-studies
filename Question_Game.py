from typing import Text
Text = ('\"Question Game\"')
print ('Welcome To The', end= ' '), print('\033[94m''\033[4m' + Text + '\033[0m', end='!' )
print ()
# Colour Question
Colour = input ('Name your favourite colour! ')
# enter hexidecimal colour value (eg #bee1e6)
print ('What colour did you choose?','\033[91m' + Colour + '\033[0m', end='!' ' ' ), print('Ah, Hexideciaml I see!')
print ()
# Triva Question
Triva = input('What programming language is named after a snake? ') 
# Type Python
print ('The anwser is:', '\033[1m''\033[36m' + Triva + '\033[0m', end='!' ' ' ), print ('Correct!')
print ()
# Scripure Question
Scripture = input('Would you mind sharing your favourite scripure with us? ')
# Enter scripure
print ('And it is:','\x1B[3m''\033[93m' + Scripture + '\033[0m''\x1B[0m', end= '.' ' '), print('Good one!')