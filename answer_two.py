import re

text = input("Type the text:")

# This is a list of profanity to check for
profanity = ["fuck", "bitch", "shit"]
profa=[]
# This splits the words of the input_text string into a list
split_txt = re.split(r"\s+", text)

# This needs to create a list of all the profanity words in input_text
for i in profanity:
    prof = re.findall(r"{i}", text)
    profa.append(i)
# This removes all the profanity words found from the text
for j in prof:
    split_txt.remove(j)

# This joins the elements of the split_text back into a string
result = " ".join(split_txt)

print(profa)
print(result)
