class Word:
    def __init__(self, text):
        self.__text = text

    def reverse_words(self):
        words = self.__text.split()
        words.reverse()         
        return " ".join(words)

user_input = input("Enter a string: ")
reverse = Word(user_input)
result = reverse.reverse_words()
print("Reversed string:", result)

        




 