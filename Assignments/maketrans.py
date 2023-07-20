# 28 
text: str = 'That is an example.' 
table = text.maketrans('h', '🙂')

print(table)
print(text.translate(table))