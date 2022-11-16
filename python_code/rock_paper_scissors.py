import random


class RockPaperScissors:

    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.player_score: int = 0
        self.opponent_score: int = 0
        self.player_choice = ""
        self.opponent_choice = ""

    def get_opponent_choice(self) -> None:
        """
        randomly generate opponent choice
        :return:
        """
        self.opponent_choice = random.choice(self.options)
        print("Opponent chose: ", self.opponent_choice)

    def get_player_choice(self) -> bool:
        """
        get a valid input for a player's choice
        0,1,2 for choices and 3 to end game
        :return: False if user wants to end the game
        """
        while True:
            try:
                num: int = int(input("Enter 0 for 'Rock', 1 for 'Paper',  2 for 'scissors', 3 to end gamec"))
                if num < 0:
                    print("Error, Try again.")
                    continue
                if num == 3:
                    return False
                self.player_choice = self.options[num]
                break
            except IndexError:
                print("Error, Try Again.")
            except ValueError:
                print("Error, Try Again.")
        return True

    def user_rock_win(self) -> None:
        """
        method for when player enters rock
        :return:
        """
        if self.opponent_choice == "paper":
            self.opponent_score += 1
            print("Paper covers rock, You Lose")
        else:
            self.player_score += 1
            print("Paper smashes scissors! You Win!")


    def user_paper_win(self) -> None:
        """
        method for when player choice is paper to see if they won or not
        :return:
        """
        if self.opponent_choice == "scissors":
            self.opponent_score += 1
            print("Scissors cut paper, You Lose")
        else:
            self.player_score += 1
            print("Paper covers rock! You Win!")

    def user_scissors_win(self) -> None:
        """
        method for when player choice is scissors to see if they won or not
        :return:
        """
        if self.opponent_choice == " rock":
            self.opponent_score += 1
            print("Rock crushes scissors, You Lose")
        else:
            self.player_score += 1
            print("Scissors cuts paper! You Win!")

    def play_game(self):
        """
        method to play the game
        get player and opponent choices see who won, update the score, and print out the scores
        :return:
        """
        print("Welcome to Rock Paper Scissors")
        while True:
            if not self.get_player_choice():
                if self.player_score > self.opponent_score:
                    print("You win! Congrats!")
                elif self.player < self.opponent_score:
                    print("You Lose")
                else:
                    print("Draw")
                break
            self.get_opponent_choice()
            if self.opponent_choice == self.player_choice:
                print("Draw")
            elif self.player_choice == "rock":
                self.user_rock_win()
            elif self.player_choice == "paper":
                self.user_paper_win()
            elif self.player_choice == "scissors":
                self.user_scissors_win()
            print("Your Score:", self.player_score)
            print("Opponent Score:", self.opponent_score)
            print()


rock = RockPaperScissors()
print(rock.play_game())