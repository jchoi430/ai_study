from abc import ABC, abstractmethod

class Choice(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """The string representation of the choice."""
        pass

    @abstractmethod
    def compare(self, other: 'Choice') -> int:
        """
        Compare this choice to another choice.
        Returns:
            1 if this choice wins
            -1 if this choice loses
            0 if it's a tie
        """
        pass
        
    def __str__(self):
        return self.name

class Rock(Choice):
    @property
    def name(self) -> str:
        return "Rock"

    def compare(self, other: Choice) -> int:
        if isinstance(other, Rock):
            return 0
        elif isinstance(other, Scissors):
            return 1  # Rock crushes scissors
        elif isinstance(other, Paper):
            return -1 # Rock covered by paper
        return 0

class Paper(Choice):
    @property
    def name(self) -> str:
        return "Paper"

    def compare(self, other: Choice) -> int:
        if isinstance(other, Paper):
            return 0
        elif isinstance(other, Rock):
            return 1  # Paper covers rock
        elif isinstance(other, Scissors):
            return -1 # Paper cut by scissors
        return 0

class Scissors(Choice):
    @property
    def name(self) -> str:
        return "Scissors"

    def compare(self, other: Choice) -> int:
        if isinstance(other, Scissors):
            return 0
        elif isinstance(other, Paper):
            return 1  # Scissors cut paper
        elif isinstance(other, Rock):
            return -1 # Scissors crushed by rock
        return 0

class Score:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.history = []  # List of historical match strings
        
    def record_match(self, user_choice: Choice, computer_choice: Choice, result: int):
        if result == 1:
            self.user_wins += 1
            outcome = "User won"
        elif result == -1:
            self.computer_wins += 1
            outcome = "Computer won"
        else:
            self.ties += 1
            outcome = "Tie"
            
        history_entry = f"{user_choice} vs {computer_choice} -> {outcome}"
        self.history.append(history_entry)
        
        # Keep only the last 10 entries to avoid overflow
        if len(self.history) > 10:
            self.history.pop(0)

def get_choice(num: int) -> Choice:
    """Helper to convert numeric input to Choice object"""
    if num == 1:
        return Rock()
    elif num == 2:
        return Paper()
    elif num == 3:
        return Scissors()
    raise ValueError("Invalid choice")
