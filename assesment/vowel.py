def get_vowels(String):
    return [each for each in String if each in "aeiou"]


word = input("Enter a word to check vowels : ")
print(get_vowels(word))
