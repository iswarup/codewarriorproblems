

# Print the word with more than one occurrence from the given String

string = input().lower().split()

ansList = []
for word in string:
	if string.count(word)>1 and word not in ansList:
		ansList.append(word)

print(ansList)