#
# CIS-125
#
# Converting Files to Pig Latin
#
# author_'Devin Simoneaux'

# Define a function called piggy(string) that returns a string

def piggy(word):
	vowels = "aeiouAEIOU"
	n = 0
	endWord = ""
	pig = ""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			if n == 0:
				pig = word + "yay"
			else:
				pig = word[n:] + endWord + "ay"
			break
		else:
			# False? Consonant
			endWord = endWord + letter
			n = n + 1
	return pig

# Open the file *getty.txt* for reading.  
myFile = open("getty.txt", "r")
# Open a new file *piggy.txt* for writing.  
newFile = open("piggy.txt", "w")
# Read the getty.txt file into a string.  
data = myFile.read()
# Strip out bad characters (, - .).
data = data.replace(",", "")
data = data.replace("-", "")
data = data.replace(".", "")
# Split the string into a list of words.  
data = data.split()
# Create a new empty string.  
newData = ""
# Loop through the list of words, pigifying each one.  
for word in data:
	newData = newData + piggy(word) + " "
# Write the new string to piggy.txt.  
newFile.write(newData)
# close the files.
myFile.close()
newFile.close()