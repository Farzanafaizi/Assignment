# 29
text: str = 'Hello Maro.' 
table = text.maketrans('M', 'F' )

print(table)
print(text.translate(table))