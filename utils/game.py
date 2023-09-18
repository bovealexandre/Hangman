from random import choice
from keyboard import read_event, KeyboardEvent
from time import sleep
from re import match


class Hangman:
    """
    Hangman game class that allows players to guess a random word by inputting letters.

    Attributes:
        possible_words (list[str]): List of possible words for the game.
        word_to_find (list[str]): The word that the player needs to guess, represented as a list of letters.
        lives (int): Number of lives or attempts the player has.
        correctly_guessed_letters (list[str]): List to track correctly guessed letters in the word.
        wrongly_guessed_letters (list[str]): List to track incorrectly guessed letters.
        turn_count (int): Number of turns taken by the player.
        error_count (int): Number of errors made by the player.

    Methods:
        play(self): Allows the player to input a letter and updates game state accordingly.
        start_game(self): Starts the game and continues until the player wins or loses.
        game_over(self): Displays a message when the game is over.
        well_played(self): Displays a message when the player successfully guesses the word.
    """

    def __init__(self) -> None:
        """
        Initializes a new Hangman game instance.
        """
        self.possible_words: list[str] = [
            "becode",
            "learning",
            "mathematics",
            "sessions",
        ]
        self.word_to_find: list[str] = [
            letter for letter in choice(self.possible_words)
        ]
        self.lives: int = 5
        self.correctly_guessed_letters: list[str] = [
            "_" for letter in self.word_to_find
        ]
        self.wrongly_guessed_letters: list[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def __str__(self):
        """
        Returns a string representation of the current Hangman game state.

        Returns:
            str: A string displaying the current word, correctly guessed letters, lives left, and wrong guesses.
        """
        word_display = " ".join(self.correctly_guessed_letters)
        return f"Word: {word_display}\nLives: {self.lives}\nWrong guesses: {', '.join(self.wrongly_guessed_letters)}"

    def play(self) -> None:
        """
        Allows the player to input a letter and updates the game state accordingly.
        """
        while True:
            print("enter a key :")
            event: KeyboardEvent = read_event()
            sleep(0.2)
            print(f"{event.name} key was pressed")
            if (
                event.name in self.correctly_guessed_letters
                or event.name in self.wrongly_guessed_letters
            ):
                print("Press a letter you didn't already press")
                continue
            if not match("[a-z]", event.name):
                print("press a letter")

            self.turn_count += 1
            letter_found = False
            for i, letter in enumerate(self.word_to_find):
                if letter == event.name:
                    self.correctly_guessed_letters[i] = event.name
                    letter_found = True

            if not (letter_found):
                self.wrongly_guessed_letters.append(event.name)
                self.lives -= 1
                self.error_count += 1
            break

    def start_game(self) -> None:
        """
        Starts the Hangman game and continues until the player wins or loses.
        """
        while True:
            print(self)
            if self.lives == 0:
                self.game_over()
                break
            elif not ("_" in self.correctly_guessed_letters):
                self.well_played()
                break
            self.play()

    def game_over(self) -> None:
        """
        Displays a message when the game is over.
        """
        print("game over ...")

    def well_played(self) -> None:
        """
        Displays a message when the player successfully guesses the word.
        """
        print(
            f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!"
        )
