import re

#words.txt is a random dictionary that I found on github.com

with open ("words.txt", "r") as myfile:
	data = myfile.read()

# print(data)

# How many words in the dictionary contain "a" (not necessarily the first letter) followed by 3-5 characters, then "b" followed by 3-5 characters, then "c"?
match1 = re.compile(r"a.{3,5}b.{3,5}c.{3,5}")
output1 = match1.findall(data)
print("Output1: ", output1)

# What is the last word in the dictionary that contains "ee" and also "oo", in that order, but not necessarily adjacent?
match2 = re.compile(r"ee.*oo")
output2 = match2.findall(data)
print("Output2: ", output2)

# How many words in the dictionary contain either "aeu" or "au", then followed by "s"?
match3 = re.compile(r"ae?u.*s")
output3 = match3.findall(data)
print("Output3: :", output3, len(output3))