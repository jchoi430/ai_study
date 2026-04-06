import pygame
import sys
import random
from models import Score, get_choice
from board import Board
import board as bd

# Setup Game Loop
FPS = 60

def main():
    # Initialize pygame
    pygame.init()
    
    board = Board()
    clock = pygame.time.Clock()
    score = Score()
    
    # State variables
    user_choice = None
    computer_choice = None
    result_text = "Press 1 (Rock), 2 (Paper), or 3 (Scissors)"
    result_color = bd.BLACK

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    running = False
                
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    # Process Inputs
                    if event.key == pygame.K_1:
                        user_choice = get_choice(1)
                    elif event.key == pygame.K_2:
                        user_choice = get_choice(2)
                    elif event.key == pygame.K_3:
                        user_choice = get_choice(3)
                        
                    computer_choice = get_choice(random.randint(1, 3))
                    
                    # Execute polymorphic resolution
                    result = user_choice.compare(computer_choice)
                    score.record_match(user_choice, computer_choice, result)
                    
                    # Interpret Results
                    if result == 1:
                        result_text = f"You Win! {user_choice} beats {computer_choice}"
                        result_color = bd.GREEN
                    elif result == -1:
                        result_text = f"You Lose! {computer_choice} beats {user_choice}"
                        result_color = bd.RED
                    else:
                        result_text = f"Tie! Both chose {user_choice}"
                        result_color = bd.BLUE

        # Render loop delegates to Board class
        board.render(user_choice, computer_choice, result_text, result_color, score)
        
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
