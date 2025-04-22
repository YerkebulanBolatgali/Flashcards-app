import random
import json

class Flashcards:
    def __init__(self, filename="words.json"):
        self.filename = filename
        self.load_words()

    def load_words(self):
        try:
            with open(self.filename, "r") as f:
                self.words = json.load(f)
        except FileNotFoundError:
            self.words = {}

    def save_words(self):
        with open(self.filename, "w") as f:
            json.dump(self.words, f, indent=4)

    def add_word(self, word, translation):
        self.words[word] = translation
        self.save_words()
        print(f"'{word}' added successfully!")

    def quiz(self):
        if not self.words:
            print("No words to practice.")
            return

        words = list(self.words.items())
        random.shuffle(words)
        correct = 0

        for word, translation in words:
            answer = input(f"Translate '{word}': ")
            if answer.strip().lower() == translation.lower():
                print("Correct!")
                correct += 1
            else:
                print(f"Wrong. Correct answer: {translation}")

        print(f"You got {correct}/{len(words)} correct.")

    def menu(self):
        while True:
            print("\n=== Flashcards Menu ===")
            print("1. Add new word")
            print("2. Practice")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                word = input("Enter the word: ")
                translation = input("Enter the translation: ")
                self.add_word(word, translation)
            elif choice == "2":
                self.quiz()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = Flashcards()
    app.menu()

