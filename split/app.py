#word Tokenization
sudlanan = []
word = ""
words = input("Enter a sentences (with spaces): ")
for i in words:
    if i == " ":
        sudlanan.append(word)
        word = ""
    else:
        word += i
sudlanan.append(word)
print(sudlanan)

#sentence tokenization
