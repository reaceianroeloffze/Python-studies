# Words to fiill in:
print ('Please Fill in the Following:')
Adjective1 = input('Adjective: ')
Animal = input('Animal: ')
Verb1 = input('Verb: ')
Exclamation1 = input('Exclamation: ')
Verb2 = input('Verb: ')
Verb3 = input('Verb: ')
Book = input('Book: ')
Exclamation2 = input('Exclamation: ')
Nonexistent_Word = input('Nonexistent Word: ')
Place1 = input('Place: ')
Game = input('Game: ')
Place2 = input('Place: ')
Adjective2 = input('Adjective: ')
Noun = input('Noun: ')
Flower = input('Flower: ')
Car = input('Car: ')

# --- Output Code ---
LibStory = f'The other day, I was really in trouble. It all started when I saw a very {Adjective1} {Animal} {Verb1} down the hallway. "{Exclamation1.capitalize()}!" I yelled. But all I could think to do was to {Verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {Verb3} right in front of my family. Then an eerie-looking grimoire titled, "{Book.title()}" fell on my head. "{Exclamation2.capitalize()}!", I exclaimed, rubbing my head. The grimoire then opened and the word "{Nonexistent_Word.upper()}" appeared before me. I pondered on the meaning when suddenly a call from {Place1.capitalize()} beckoned me. I was invited for a game of {Game.title()} with the Duke of {Place2.capitalize()} who was a rather {Adjective2.lower()} fellow. I was antsy throughout the whole experience but nevertheless it was wonderful for the {Noun}. Now all that remains is to tether the {Flower.capitalize()} to the {Car.upper()}.'
print ('\033[92m''\033[3m''\033[1m' + LibStory + '\033[0m')

