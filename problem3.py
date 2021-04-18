

# Find the first non-repeating character in a given String

string = input()

if len(string) == 0:
		print("The string is empty")
else:
	for i in string:

		if string.count(i) == 1:
			print(f"The first non-repeating character is '{i}'.")
			break

	else:
		print("All characters occur more than once.")