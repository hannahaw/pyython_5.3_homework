import string

text = input()
text = text.title()
clean_text = ''

for char in text:
    if char != ' ' and char not in string.punctuation:
        clean_text += char

hashtag = '#' + clean_text
print(hashtag[:140])
