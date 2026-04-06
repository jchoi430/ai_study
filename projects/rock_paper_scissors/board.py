import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (50, 100, 200)
RED = (200, 50, 50)
GREEN = (50, 180, 50)

class Board:
    def __init__(self, width=600, height=500):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Rock, Paper, Scissors")
        
        # Fonts (fallback logic included)
        try:
            self.font_large = pygame.font.SysFont("arial", 48, bold=True)
            self.font_med = pygame.font.SysFont("arial", 32)
            self.font_small = pygame.font.SysFont("arial", 20)
        except:
            self.font_large = pygame.font.Font(None, 48)
            self.font_med = pygame.font.Font(None, 32)
            self.font_small = pygame.font.Font(None, 20)

    def draw_text_center(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_text_left(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        self.screen.blit(text_obj, (x, y))

    def render(self, user_choice, computer_choice, result_text, result_color, score):
        # Render background
        self.screen.fill(WHITE)
        
        # Top: Title & Instructions
        self.draw_text_center("Rock, Paper, Scissors", self.font_large, BLACK, self.width//2, 40)
        self.draw_text_center("(1) Rock  |  (2) Paper  |  (3) Scissors  |  (0) Quit", self.font_small, GRAY, self.width//2, 80)
        
        # Middle: Scoreboard
        pygame.draw.line(self.screen, GRAY, (50, 110), (self.width-50, 110), 2)
        
        # Center the user / computer scores
        self.draw_text_left(f"User: {score.user_wins}", self.font_med, GREEN, 80, 130)
        self.draw_text_left(f"Computer: {score.computer_wins}", self.font_med, RED, 350, 130)
        self.draw_text_center(f"Ties: {score.ties}", self.font_small, BLUE, self.width//2, 175)
        
        pygame.draw.line(self.screen, GRAY, (50, 205), (self.width-50, 205), 2)
        
        # Action Results (Right below scoreboard)
        if user_choice and computer_choice:
            self.draw_text_center(result_text, self.font_med, result_color, self.width//2, 240)
        else:
            self.draw_text_center(result_text, self.font_med, BLACK, self.width//2, 240)
            
        # Bottom: Recent Matches History
        self.draw_text_left("Recent Matches:", self.font_med, BLACK, 60, 290)
        
        # Show max 6 history lines on screen (newest on top)
        for i, match in enumerate(reversed(score.history[-6:])):
            self.draw_text_left(f"- {match}", self.font_small, BLACK, 80, 330 + (i * 25))
            
        pygame.display.flip()
