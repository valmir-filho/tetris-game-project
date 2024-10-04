from colors import Colors   # Import Colors for color constants.
from game import Game       # Import the Game class to handle game state and mechanics.
import pygame, sys

pygame.init()  # Initialize Pygame.
# Font and text surfaces for rendering score, next block, and "game over" message.
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
# Rectangles for positioning the score and next block display.
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
# Create the game window.
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")
# Game clock for controlling the frame rate.
clock = pygame.time.Clock()
# Create the game object from the Game class (this object controls game state).
game = Game()
# Custom Pygame event for updating the game at regular intervals.
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)  # Update every 200ms.

# Main game loop.
while True:
    # Event handling loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if the window is closed.
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:  # Reset the game if it's over and a key is pressed.
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()  # Move the piece left.
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()  # Move the piece right.
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()  # Move the piece down.
                game.update_score(0, 1)  # Increment score for a soft drop.
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()  # Rotate the piece.
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()  # Automatically move the piece down periodically.
    # Drawing the game.
    score_value_surface = title_font.render(str(game.score), True, Colors.white)  # Render the current score.
    screen.fill(Colors.dark_blue)  # Clear the screen with a background color.
    screen.blit(score_surface, (365, 20, 50, 50))  # Draw the "Score" label.
    screen.blit(next_surface, (375, 180, 50, 50))  # Draw the "Next" label.
    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))  # Display "Game Over" if the game is over.
    # Draw the score box with rounded corners.
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, 
                                                                  centery=score_rect.centery))
    # Draw the next block box.
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    # Draw the game state (grid and falling piece).
    game.draw(screen)
    # Update the display with the latest changes.
    pygame.display.update()
    # Cap the frame rate at 60 frames per second.
    clock.tick(60)
