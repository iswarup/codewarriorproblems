
# Find the maximum occurring character in a given String

string = input()

# Creating a dictionary to keep track of number of occurences of each charachter.
counts = {}

for char in string:
	if char in counts:
		counts[char]+=1
	else:
		counts[char]=1

# print(counts)
maxCount = max(counts, key=counts.get)

print(f"Letter '{maxCount}' occurs {counts[maxCount]} number of times.")