# 
# File Header
#
# Define vowels



# Loop through word, one letter at a time

word = input("Please enter a word: ")	
endWord = ""
vowels = "aeiouAEIOU"
n = 0
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


print (pig)