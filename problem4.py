'''
Print all strings of maximum length from an array of strings.

Input: arr = [code,home,water,food,keras] Output: [keras,water]'''

words = input().split()

lengths = {}

for word in words:
	lengths[word] = len(word)

maxLength = max(lengths.values())

for word,length in lengths.items():
	if maxLength == length:
		print(word, end=" ")

print()