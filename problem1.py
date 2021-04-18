
# Find the maximum occurring character in a given String

string = input()

counts = {}

for char in string:
	if char in counts:
		counts[char]+=1
	else:
		counts[char]=1

# print(counts)
maxCount = max(counts, key=counts.get)

print(maxCount, counts[maxCount])