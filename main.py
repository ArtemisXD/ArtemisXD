print("hello world")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

name = input("What is the characters name?\n")
age = input("What is the characters age?\n")
print("My name is " + name  + ".")
print("My age is " + age + ".")

sentenceUpper = "Hi I ReALLY lIke OraNgEs"
print(sentenceUpper.upper().isupper())

print(sentenceUpper.upper().replace("ORANGES", "APPLES"))

sentenceLength = "[owfj'awfafasjIGW|+w\j]g21]2j-213gj3k"
print(len(sentenceLength))

wordSearch = input("What position word would you like to find in this string?")
while not wordSearch.isdigit():
    print("That isn't a whole number.")
    wordSearch = input("What position word would you like to find in this string?")
wordSearch = int(wordSearch)
print(sentenceLength[wordSearch])


