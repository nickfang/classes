import re
import exerciseUtils as eu

# Find all words that contain either "oo" or "ee" immediately after the letter "r" and before any of the letters "p", "s", or "t".
match1 = re.compile(r"r(oo|ee)[pst]")
print("Match1: ", eu.searchWords(match1))
# Find words in the dictionary that start with "b" and have either three vowels or three consonants (i.e., non-vowels) in a row.
match2 = re.compile(r"^b([aeiou]{3}|[^aeiou]{3})")
print("Match2: ", eu.searchWords(match2))
# Find words that contain, inside of them, the words "small", "medium", or "large".
match3 = re.compile(r"(small|medium|large)")
print("Match3: ", eu.searchWords(match3))