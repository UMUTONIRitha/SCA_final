import re
input_text = input("Type your statement.")

# This is a list of profanity to check for
profanity = ["fuck", "bitch", "shit"]

# This splits the words of the input_text string into a list
split_text = re.findall(r"\w+", input_text)
result = [];
# This needs to create a list of all the profanity words in input_text
for x in profanity:
    if x in split_text:
        result.append(x)

print(result)
