#There are two lists, letters and points that contain the letters and their respective points that these letters are worth for

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#These are combined into a dictionary using a list comprehension namely, letter_to_points, that has letters as the keys and points as the values

letter_to_points = {key:value for key,value in zip(letters,points)}
print(letter_to_points)

#include blank spaces into account too

letter_to_points[" "] = 0

#a function that will take in a word and return how many points that word is worth.

def score_words(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i, 0)
  return point_total

#We expect the word BROWNIE to earn 15 points, let's check it out.

brownie_points = score_words("BROWNIE")
print(brownie_points)

# mapping of players to how many points they’ve scored.
 
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

#a function that would take in a player and a word, and add that word to the list of words they’ve played

def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for i in words:
      player_points+=score_words(i.upper())
    player_to_points[player] = player_points
  print(player_to_points)

def play_word(player,word):
  player_to_words.get(player).append(word)
  
#let's check the above functions and the current leaderboard
play_word("player1","NOVICE")
update_point_totals()