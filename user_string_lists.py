"""
Modify this docstring.

"""

# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

#last name of popular/historic male tennis players
list_mens_players = ["Djokovic", "Nadal", "Federer", "Alcaraz", "Zverev"]
#last name of popular/historic female tennis players
list_womens_players = ["Williams", "Williams", "King", "Graf", "Sabalenka"]
#famous tennis product brands
list_tennis_brands = ["Wilson", "Head", "Penn", "Babolat", "Dunlop"]
#names of the major grand slam tournaments
list_grand_slams = ["US Open", "French Open", "Wimbledon", "Australian Open"]
#types of court surfaces
list_court_types = ["grass", "clay", "hard"]

#String Lists 1. Using Python Built-in Functions
#using zip()
mens_womens_tuple = list(zip(list_mens_players, list_womens_players))
print(mens_womens_tuple)
#using len() and zip()
min_len = min(len(list_tennis_brands), len(list_grand_slams), len(list_court_types))
brands_slams_types = list(zip(list_tennis_brands[:min_len], list_grand_slams[:min_len], list_court_types[:min_len]))
print(brands_slams_types)
#using set()
mens_brands = set(zip(list_mens_players, list_tennis_brands))
print(mens_brands)

#String Lists 2. Random choice
import random
random_womens_player = random.choice(list_womens_players)
print(random_womens_player)

lists_verbs = ["runs", "swings", "shuffles", "jumps", "uses"]
lists_adjectives = ["quickly", "powerfully", "athletically"]
lists_nouns = ["ball", "racquet", "net", "opponent"]
lists_outcome = ["wins", "loses", "ties"]

mens_players = random.choice(list_mens_players)
womens_players = random.choice(list_womens_players)
grand_slams = random.choice(list_grand_slams)
verb = random.choice(lists_verbs)
adjective = random.choice(lists_adjectives)
noun = random.choice(lists_nouns)
outcome = random.choice(lists_outcome)

sentence_1 = f"{womens_players} {outcome} against {mens_players}."
sentence_2 = f"{mens_players} {verb} the {noun} {adjective}."
sentence_3 = f"{womens_players} {outcome} {grand_slams}!"

print(sentence_1)
print(sentence_2)
print(sentence_3)

#String Lists 3. Get Unique Words
import re
with open('text_hamlet.txt', 'r') as file:
     text = file.read()
words = re.findall(r'\b\w+\b', text.lower())
#findall executes same function of split
unique_words = set(words)
print(len(unique_words))

#This list is good?