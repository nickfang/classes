import re
import exerciseUtils as eu

# Find all words in the dictionary that start with a capital vowel and contain at least 8 letters
match1 = re.compile(r"^[A-Z]/w{7,}")
print("Match1: ", eu.searchWords(match1))
# Find all words in the dictionary whose first letter isn't capitalized, whose second letter is a vowel, and whose third-to-last letter is either "x", "y", or "z"
match2 = re.compile(r"^[a-z][aeiou]\w*[xyz]\w\w$")
print("Match2: ", eu.searchWords(match2))
# Find all words in the dictionary that contain three vowels in a row, but in which that three-vowel sequence is at least 5 characters after the front of the word and also 5 characters before the end of the word.
match3 = re.compile(r"^\w{5,}[aeiou]{3}\w{5}$")
print("Match3: ", eu.searchWords(match3))