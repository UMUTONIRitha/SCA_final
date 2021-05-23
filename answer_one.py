# Python Program to remove a profanity word
# with empty space in a sentence


# Function takes two parameter
def remove(text, profanity):

	# Break down sentence by ' ' spaces
	# and store each individual word in
	# a different list
	word_list = text.split()

	# A new string to store the result
	result = ''

	# Creating the variable which is a empty space
	# "*" text of the length of removed  word
	emptySpace = '' * len(profanity)

	# count variable to
	# access our word_list
	count = 0

	# Iterating through our list
	# of extracted words
	index = 0;
	for i in word_list:

		if i == profanity[0] or i == profanity[1] :
			
			# changing the censored word to
			# created asterisks censor
			word_list[index] = emptySpace
            
		index += 1
        
	# join the words
	result =' '.join(word_list)

	return result

# Driver code
if __name__== '__main__':
	
	extract = "GeeksforGeeks is a fuck science portal.\
			I am pursuing my major in bitch science. "			
	rem = ["fuck", "bitch"]	
	print(remove(extract, rem))
