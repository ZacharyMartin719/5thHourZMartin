#Name: Zachary Martin
#Assignment: Ai Playground


import pygame
import random
'''

#Shooting Game 
# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Target class
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(50, 200)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed = -self.speed

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
targets = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Create targets
for _ in range(5):
    target = Target()
    all_sprites.add(target)
    targets.add(target)

# Game loop
running = True
score = 0
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a bullet when space is pressed
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update all sprites
    all_sprites.update()

    # Check for collisions between bullets and targets
    for bullet in bullets:
        target_hits = pygame.sprite.spritecollide(bullet, targets, True)
        if target_hits:
            bullet.kill()
            score += 1
            print(f"Score: {score}")
            target = Target()
            all_sprites.add(target)
            targets.add(target)

    # Draw everything
    all_sprites.draw(screen)

    # Display score
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()

# Drawing Game 
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Painting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the clock
clock = pygame.time.Clock()

# Define the brush size
brush_size = 5

# Create a surface for drawing
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
drawing_surface.fill(WHITE)  # Set the background color to white

# Create a variable to track if the user is drawing
drawing = False

# Brush color variable
current_color = BLACK

# Game loop
while True:
    screen.fill(WHITE)  # Clear the screen with white background

    # Draw the drawing surface
    screen.blit(drawing_surface, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse button press to start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True

        # Mouse button release to stop drawing
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False

        # Keyboard events for color change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Press 'r' to change to red
                current_color = RED
            elif event.key == pygame.K_g:  # Press 'g' to change to green
                current_color = GREEN
            elif event.key == pygame.K_b:  # Press 'b' to change to blue
                current_color = BLUE
            elif event.key == pygame.K_y:  # Press 'y' to change to yellow
                current_color = YELLOW
            elif event.key == pygame.K_k:  # Press 'k' to change to black
                current_color = BLACK
            elif event.key == pygame.K_c:  # Press 'c' to clear the screen
                drawing_surface.fill(WHITE)

    # If the mouse is pressed, draw on the surface
    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(drawing_surface, current_color, (mouse_x, mouse_y), brush_size)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

#Farming Game
import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Farming Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
DARK_GREEN = (34, 139, 34)
LIGHT_GREEN = (144, 238, 144)
BLUE = (0, 0, 255)

# Set up fonts
font = pygame.font.SysFont(None, 30)

# Tile size
TILE_SIZE = 60
TILE_GAP = 5

# Crop states
EMPTY = 0
PLANTED = 1
WATERED = 2
GROWN = 3

# Set up the clock
clock = pygame.time.Clock()

# Crop class
class Crop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.state = EMPTY
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.growth_time = random.randint(3, 6)  # Time it takes to grow in seconds
        self.time_planted = time.time()

    def update(self):
        if self.state == PLANTED:
            if time.time() - self.time_planted > 1:  # Update every second
                self.state = WATERED if self.state == PLANTED else GROWN

        if self.state == WATERED:
            self.image.fill(LIGHT_GREEN)

        if self.state == GROWN:
            self.image.fill(DARK_GREEN)

    def water(self):
        if self.state == PLANTED:
            self.state = WATERED
            self.time_planted = time.time()  # Reset growth timer

    def harvest(self):
        if self.state == GROWN:
            self.state = EMPTY
            return True
        return False

# Create a list to hold all the crops
crops = []

# Create the grid of crops
for row in range(5):
    for col in range(5):
        crop = Crop(col * (TILE_SIZE + TILE_GAP), row * (TILE_SIZE + TILE_GAP))
        crops.append(crop)

# Game loop
score = 0
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for crop in crops:
                if crop.rect.collidepoint(mouse_x, mouse_y):
                    if event.button == 1:  # Left mouse button
                        if crop.state == EMPTY:
                            crop.state = PLANTED
                            crop.time_planted = time.time()
                    elif event.button == 3:  # Right mouse button (for watering)
                        if crop.state == PLANTED:
                            crop.water()
                    elif event.button == 2:  # Middle mouse button (for harvesting)
                        if crop.harvest():
                            score += 1

    # Update crops and draw them
    for crop in crops:
        crop.update()
        screen.blit(crop.image, (crop.x, crop.y))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)


#Two Player game
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Player Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

# Ball settings
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Score variables
score_player1 = 0
score_player2 = 0

# Set up fonts
font = pygame.font.SysFont(None, 40)

# Create paddles and ball
player1_paddle = pygame.Rect(30, (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(SCREEN_WIDTH - 30 - PADDLE_WIDTH, (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Ball velocity
ball_velocity_x = BALL_SPEED_X
ball_velocity_y = BALL_SPEED_Y

# Function to display the score
def display_score():
    score_text = font.render(f"{score_player1} - {score_player2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()

    # Player 1 controls (W = up, S = down)
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < SCREEN_HEIGHT:
        player1_paddle.y += PADDLE_SPEED

    # Player 2 controls (Up Arrow = up, Down Arrow = down)
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < SCREEN_HEIGHT:
        player2_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_velocity_x
    ball.y += ball_velocity_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_velocity_y *= -1  # Reverse the ball's vertical direction

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_velocity_x *= -1  # Reverse the ball's horizontal direction

    # Scoring
    if ball.left <= 0:  # Player 2 scores
        score_player2 += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_RADIUS
        ball.y = SCREEN_HEIGHT // 2 - BALL_RADIUS
        ball_velocity_x *= -1  # Reset ball direction

    if ball.right >= SCREEN_WIDTH:  # Player 1 scores
        score_player1 += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_RADIUS
        ball.y = SCREEN_HEIGHT // 2 - BALL_RADIUS
        ball_velocity_x *= -1  # Reset ball direction

    # Draw paddles, ball, and score
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    display_score()

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second


# 8 Ball Pool Game
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8 Ball Pool')

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def check_wall_collision(self):
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -1

    def apply_friction(self):
        friction = 0.98
        self.vx *= friction
        self.vy *= friction

    def check_collision(self, other_ball):
        dx = self.x - other_ball.x
        dy = self.y - other_ball.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + other_ball.radius:
            angle = math.atan2(dy, dx)
            total_mass = 2 * self.radius

            # Elastic collision
            self.vx -= math.cos(angle) * total_mass
            self.vy -= math.sin(angle) * total_mass
            other_ball.vx += math.cos(angle) * total_mass
            other_ball.vy += math.sin(angle) * total_mass

# Create the balls
balls = [Ball(100, 100, 15, WHITE),  # Cue ball
         Ball(400, 200, 15, RED),    # 8 Ball
         Ball(200, 200, 15, GREEN)]  # Example other ball

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball movement logic
    for ball in balls:
        ball.move()
        ball.check_wall_collision()
        ball.apply_friction()

    # Collision between balls
    for i, ball in enumerate(balls):
        for j, other_ball in enumerate(balls):
            if i != j:
                ball.check_collision(other_ball)

    # Draw balls
    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()

    # Set FPS
    clock.tick(60)

pygame.quit()


# BasketBall Game
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Basketball Game")

# Game variables
basketball_radius = 15
basketball_color = RED
ball_x = WIDTH // 4
ball_y = HEIGHT - 50
ball_vx = 0
ball_vy = 0
gravity = 0.5
is_shooting = False
score = 0

# Hoop variables
hoop_radius = 30
hoop_x = WIDTH - 100
hoop_y = HEIGHT // 2
hoop_width = 100
hoop_height = 10

# Function to draw the basketball hoop
def draw_hoop():
    pygame.draw.rect(screen, BLUE, (hoop_x - hoop_width // 2, hoop_y - hoop_height // 2, hoop_width, hoop_height))

# Function to draw the basketball
def draw_ball(x, y):
    pygame.draw.circle(screen, basketball_color, (x, y), basketball_radius)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    draw_hoop()
    draw_ball(ball_x, ball_y)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start shooting when mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_shooting:
                # Calculate angle and power based on mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - ball_x
                dy = mouse_y - ball_y
                angle = math.atan2(dy, dx)
                power = min(math.hypot(dx, dy) / 10, 20)  # Power of the shot

                # Set velocity based on the calculated angle and power
                ball_vx = power * math.cos(angle)
                ball_vy = power * math.sin(angle)
                is_shooting = True

    # Ball movement logic
    if is_shooting:
        ball_x += ball_vx
        ball_y += ball_vy
        ball_vy += gravity  # Apply gravity

        # Ball collision with the floor (bounce)
        if ball_y + basketball_radius >= HEIGHT:
            ball_y = HEIGHT - basketball_radius
            ball_vy *= -0.6  # Reduce velocity to simulate bounce

        # Check if the ball goes through the hoop
        if (ball_x > hoop_x - hoop_width // 2 and
            ball_x < hoop_x + hoop_width // 2 and
            ball_y - basketball_radius <= hoop_y + hoop_height // 2 and
            ball_y + basketball_radius >= hoop_y - hoop_height // 2):
            score += 1
            is_shooting = False
            ball_x = WIDTH // 4
            ball_y = HEIGHT - 50
            ball_vx = 0
            ball_vy = 0

    # Display the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set FPS
    clock.tick(FPS)

pygame.quit()


#Gambling Game
import random

# Define card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Values of cards
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
               'A': 11}


# Card deck
def create_deck():
    return [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]


# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)


# Calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(card_values[card['rank']] for card in hand)
    ace_count = sum(1 for card in hand if card['rank'] == 'A')

    # Adjust for aces (count as 1 if needed)
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1

    return value


# Print cards in hand
def print_hand(name, hand):
    print(f"{name}'s hand: ", ', '.join([f"{card['rank']} of {card['suit']}" for card in hand]))


# Check if player wants to hit or stand
def player_turn(deck, player_hand, player_money, bet_amount):
    while True:
        print_hand("Your", player_hand)
        player_value = calculate_hand_value(player_hand)
        print(f"Your total value: {player_value}")

        if player_value > 21:
            print("You bust!")
            return False, player_money - bet_amount  # Player loses the bet

        # Ask the player for an action
        action = input("Do you want to (H)it or (S)tand? ").strip().lower()

        if action == 'h':
            player_hand.append(deck.pop())
        elif action == 's':
            return True, player_money
        else:
            print("Invalid action. Please choose 'H' to Hit or 'S' to Stand.")


# Dealer's turn
def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print_hand("Dealer", dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's total value: {dealer_value}")
    return dealer_value


# Main game loop
def blackjack():
    player_money = 1000  # Starting money
    print("Welcome to Blackjack!")

    while player_money > 0:
        print(f"\nYou have ${player_money}.")
        bet_amount = int(input("Place your bet: $"))

        if bet_amount > player_money:
            print("You can't bet more than you have.")
            continue

        # Create and shuffle deck
        deck = create_deck()
        shuffle_deck(deck)

        # Deal initial hands
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print_hand("Dealer", [dealer_hand[0]])  # Only show one card of the dealer's hand

        # Player's turn
        success, player_money = player_turn(deck, player_hand, player_money, bet_amount)
        if not success:
            continue  # Player busts and loses bet

        # Dealer's turn
        dealer_value = dealer_turn(deck, dealer_hand)

        # Compare hands and determine winner
        player_value = calculate_hand_value(player_hand)
        if dealer_value > 21:
            print("Dealer busts! You win!")
            player_money += bet_amount
        elif player_value > dealer_value:
            print("You win!")
            player_money += bet_amount
        elif player_value < dealer_value:
            print("Dealer wins!")
            player_money -= bet_amount
        else:
            print("It's a tie!")

        # Ask player if they want to play again
        if player_money > 0:
            play_again = input("Do you want to play again? (Y/N): ").strip().lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break
        else:
            print("You ran out of money!")
            break


# Run the game
blackjack()

#Typing Game 
import random
import time

# List of words to type
word_list = [
    "python", "java", "ruby", "javascript", "html", "css", "database", "algorithm", "computer", "programming",
    "developer", "framework", "machine", "learning", "artificial", "intelligence", "network", "security", "software", "hardware"
]

# Function to select a random word
def get_random_word():
    return random.choice(word_list)

# Function to calculate typing speed
def typing_game():
    print("Welcome to the Typing Speed Game!")
    print("Your goal is to type the word as fast and accurately as possible.")
    print("Press Enter to start...")
    input()  # Wait for the user to press Enter to begin

    word = get_random_word()  # Get a random word
    print(f"\nYour word is: {word}")
    print("\nStart typing the word when you're ready!")

    start_time = time.time()  # Record the start time
    typed_word = input("Type the word: ")  # User types the word
    end_time = time.time()  # Record the end time

    time_taken = end_time - start_time  # Calculate time taken to type the word
    accuracy = calculate_accuracy(word, typed_word)  # Calculate typing accuracy

    print(f"\nYou typed: {typed_word}")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Typing accuracy: {accuracy}%")

    # Feedback based on accuracy and speed
    if accuracy == 100:
        print("Great job! Perfect accuracy!")
    elif accuracy >= 80:
        print("Well done! Good accuracy!")
    else:
        print("You can do better! Keep practicing!")

    # Offer the player to play again
    play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if play_again == 'y':
        typing_game()  # Recursively call the game again to restart
    else:
        print("Thanks for playing!")

# Function to calculate typing accuracy
def calculate_accuracy(original_word, typed_word):
    correct_chars = 0
    for o, t in zip(original_word, typed_word):
        if o == t:
            correct_chars += 1
    accuracy = (correct_chars / len(original_word)) * 100
    return accuracy

# Run the game
typing_game()
'''

import random

# 1. Text Adventure Game Framework
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def describe(self):
        print(f"You are in {self.name}. {self.description}")
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f" - {item.name}")
        else:
            print("There are no items here.")
        if self.exits:
            print("Exits:")
            for direction in self.exits:
                print(f" - {direction}")


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction} into {self.current_room.name}.")
            self.current_room.describe()
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        item_to_take = None
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                item_to_take = item
                break
        if item_to_take:
            self.inventory.append(item_to_take)
            self.current_room.items.remove(item_to_take)
            print(f"You took the {item_name}.")
        else:
            print(f"There is no {item_name} here.")

    def describe_inventory(self):
        if self.inventory:
            print("Your inventory contains:")
            for item in self.inventory:
                print(f" - {item.name}")
        else:
            print("Your inventory is empty.")

# 2. Create rooms and items
def create_rooms():
    room1 = Room("Entrance Hall", "A grand hall with towering columns and large wooden doors.")
    room2 = Room("Library", "A dusty library with rows of ancient books and mysterious scrolls.")
    room3 = Room("Garden", "A tranquil garden with blooming flowers and a small pond.")
    room4 = Room("Dungeon", "A dark and damp dungeon with chains hanging from the walls.")

    room1.add_exit("north", room2)
    room2.add_exit("south", room1)
    room2.add_exit("east", room3)
    room3.add_exit("west", room2)
    room3.add_exit("north", room4)
    room4.add_exit("south", room3)

    book = Item("Ancient Book", "A book that seems to glow faintly.")
    scroll = Item("Mysterious Scroll", "A scroll with strange markings.")
    flower = Item("Golden Flower", "A rare golden flower with an enchanting fragrance.")

    room1.add_item(book)
    room2.add_item(scroll)
    room3.add_item(flower)

    return room1

# 3. Game logic
def game_loop(player):
    while True:
        print(f"\n{player.name}'s Adventure\n")
        player.current_room.describe()
        command = input("What do you want to do? ").lower()

        if "move" in command:
            direction = command.split()[-1]
            player.move(direction)
        elif "take" in command:
            item_name = command.split()[-1]
            player.take_item(item_name)
        elif "inventory" in command:
            player.describe_inventory()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")

# 4. Main function
def main():
    player_name = input("Enter your player name: ")
    player = Player(player_name)
    starting_room = create_rooms()
    player.current_room = starting_room

    print(f"\nWelcome to the game, {player_name}!")
    print("Your adventure begins now.")

    game_loop(player)

if __name__ == "__main__":
    main()
