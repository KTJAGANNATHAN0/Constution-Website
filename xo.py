import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 20
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (255, 0, 0)  # Bright red color for X
CIRCLE_RADIUS = 100
CIRCLE_WIDTH = 20
CROSS_WIDTH = 40  # Increased thickness for better visibility
SPACE = 50  # Adjusted space to make X fit better

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)

def draw_xo(row, col, player):
    if player == 'X':
        start_x = col * WIDTH // 3 + SPACE
        start_y = row * HEIGHT // 3 + SPACE
        end_x = (col + 1) * WIDTH // 3 - SPACE
        end_y = (row + 1) * HEIGHT // 3 - SPACE

        # Draw the two lines of the "X"
        pygame.draw.line(screen, CROSS_COLOR, (start_x, start_y), (end_x, end_y), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (end_x, start_y), (start_x, end_y), CROSS_WIDTH)
    elif player == 'O':
        center_x = col * WIDTH // 3 + WIDTH // 6
        center_y = row * HEIGHT // 3 + HEIGHT // 6
        pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)



def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(cell != '' for row in board for cell in row)

def ai_move():
    # Step 1: Check if AI can win in the next move
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = ai
                if check_win(ai):
                    return r, c
                board[r][c] = ''

    # Step 2: Check if the player is about to win, and block them
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = player
                if check_win(player):
                    board[r][c] = ai
                    return r, c
                board[r][c] = ''

    # Step 3: Take one of the corners if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for r, c in corners:
        if board[r][c] == '':
            return r, c

    # Step 4: Take the center if available
    if board[1][1] == '':
        return 1, 1

    # Step 5: Take any remaining empty space
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
    if empty_cells:
        return random.choice(empty_cells)


def display_text(text, size, color, y_offset=0):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

mcq_list = [
    {
        "question": "Which article of the Indian Constitution guarantees the Right to Equality?",
        "options": ["A) Article 14", "B) Article 19", "C) Article 21", "D) Article 22"],
        "correct": "A"
    },
    {
        "question": "The Right to Freedom of Speech and Expression is provided under which article of the Indian Constitution?",
        "options": ["A) Article 15", "B) Article 19", "C) Article 21", "D) Article 25"],
        "correct": "B"
    },
    {
        "question": "Which Fundamental Right is concerned with the protection against arbitrary arrest and detention?",
        "options": ["A) Right to Equality", "B) Right to Freedom", "C) Right against Exploitation", "D) Right to Constitutional Remedies"],
        "correct": "B"
    },
    {
        "question": "Article 21 of the Indian Constitution guarantees:",
        "options": ["A) Right to Property", "B) Right to Privacy", "C) Right to Equality", "D) Right to Constitutional Remedies"],
        "correct": "B"
    },
    {
        "question": "Which of the following Fundamental Rights can be suspended during an emergency?",
        "options": ["A) Right to Equality", "B) Right to Freedom of Speech and Expression", "C) Right against Exploitation", "D) Right to Constitutional Remedies"],
        "correct": "D"
    },
    {
        "question": "The Right to Education was added to the Fundamental Rights by:",
        "options": ["A) 73rd Amendment Act", "B) 74th Amendment Act", "C) 86th Amendment Act", "D) 92nd Amendment Act"],
        "correct": "C"
    },
    {
        "question": "Which article provides for the abolition of untouchability?",
        "options": ["A) Article 15", "B) Article 17", "C) Article 18", "D) Article 25"],
        "correct": "B"
    },
    {
        "question": "The Right to Constitutional Remedies is enshrined in which article?",
        "options": ["A) Article 32", "B) Article 36", "C) Article 40", "D) Article 50"],
        "correct": "A"
    },
    {
        "question": "The Directive Principles of State Policy are primarily contained in which part of the Constitution?",
        "options": ["A) Part III", "B) Part IV", "C) Part V", "D) Part VI"],
        "correct": "B"
    },
    {
        "question": "Which of the following Directive Principles aims to promote the welfare of the people by securing a social order?",
        "options": ["A) Article 39", "B) Article 41", "C) Article 44", "D) Article 47"],
        "correct": "A"
    },
    {
        "question": "The Directive Principle that aims to establish a uniform civil code throughout the territory of India is found in which article?",
        "options": ["A) Article 40", "B) Article 42", "C) Article 43", "D) Article 44"],
        "correct": "D"
    },
    {
        "question": "Which article of the Indian Constitution directs the state to organize village panchayats?",
        "options": ["A) Article 40", "B) Article 43", "C) Article 44", "D) Article 48"],
        "correct": "A"
    },
    {
        "question": "Which amendment of the Indian Constitution is known as the Mini Constitution?",
        "options": ["A) 42nd Amendment", "B) 44th Amendment", "C) 86th Amendment", "D) 73rd Amendment"],
        "correct": "A"
    }
];



def ask_mcq():
    mcq = random.choice(mcq_list)
    screen.fill(BOARD_COLOR)

    # Split the question into multiple lines if it's too long
    question_lines = []
    max_line_length = 40  # Adjust this value based on screen width and font size

    words = mcq["question"].split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += word + " "
        else:
            question_lines.append(current_line)
            current_line = word + " "
    question_lines.append(current_line.strip())

    # Display the question
    y_offset = -100
    for line in question_lines:
        display_text(line, 30, (255, 255, 255), y_offset)
        y_offset += 40

    # Display the options
    display_text(mcq["options"][0], 35, (255, 255, 255), y_offset)
    display_text(mcq["options"][1], 35, (255, 255, 255), y_offset + 40)
    display_text(mcq["options"][2], 35, (255, 255, 255), y_offset + 80)
    display_text(mcq["options"][3], 35, (255, 255, 255), y_offset + 120)
    pygame.display.update()

    player_answer = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_answer = "A"
                elif event.key == pygame.K_b:
                    player_answer = "B"
                elif event.key == pygame.K_c:
                    player_answer = "C"
                elif event.key == pygame.K_d:
                    player_answer = "D"
                else:
                    display_text("Invalid option! Press A, B, C, or D.", 35, (255, 0, 0), y_offset + 160)
                    pygame.display.update()
                    pygame.time.wait(1500)
                    screen.fill(BOARD_COLOR)
                    
                    # Re-display the question and options after an invalid input
                    y_offset = -100
                    for line in question_lines:
                        display_text(line, 30, (255, 255, 255), y_offset)
                        y_offset += 40
                    display_text(mcq["options"][0], 35, (255, 255, 255), y_offset)
                    display_text(mcq["options"][1], 35, (255, 255, 255), y_offset + 40)
                    display_text(mcq["options"][2], 35, (255, 255, 255), y_offset + 80)
                    display_text(mcq["options"][3], 35, (255, 255, 255), y_offset + 120)
                    pygame.display.update()

        if player_answer is not None:
            break

    # Feedback display
    if player_answer == mcq["correct"]:
        display_text("Correct!", 50, (0, 255, 0), y_offset + 160)  # Green color for correct
    else:
        display_text(f"Wrong! Correct answer: {mcq['correct']}", 50, (255, 0, 0), y_offset + 160)  # Red color for wrong answer

    pygame.display.update()
    pygame.time.wait(2000)  # Wait 2 seconds before continuing

    return player_answer == mcq["correct"]



def play_again_or_exit():
    screen.fill(BOARD_COLOR)
    display_text("Play Again? (Y/N)", 50, (255, 255, 255))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

def main():
    global board, player, ai
    while True:
        board = [['' for _ in range(3)] for _ in range(3)]
        screen.fill(BOARD_COLOR)
        draw_lines()
        display_text('Press X or O to select', 50, (255, 255, 255), -100)
        pygame.display.update()

        # Player selection phase
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        player = 'X'
                        ai = 'O'
                        break
                    elif event.key == pygame.K_o:
                        player = 'O'
                        ai = 'X'
                        break
            else:
                continue
            break

        screen.fill(BOARD_COLOR)
        draw_lines()
        display_text(f'You are {player}', 50, (255, 255, 255), -100)
        pygame.display.update()
        
        running = True
        game_over = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    x, y = event.pos
                    row, col = y // (HEIGHT // 3), x // (WIDTH // 3)
                    if board[row][col] == '':
                        if ask_mcq():
                            board[row][col] = player
                        screen.fill(BOARD_COLOR)
                        draw_lines()
                        for r in range(3):
                            for c in range(3):
                                if board[r][c] != '':
                                    draw_xo(r, c, board[r][c])
                        pygame.display.update()

                        if check_win(player):
                            game_over = True
                        elif check_draw():
                            game_over = True

                        if not game_over:
                            ai_row, ai_col = ai_move()
                            if ai_row is not None:
                                board[ai_row][ai_col] = ai
                                draw_xo(ai_row, ai_col, ai)
                                pygame.display.update()

                                if check_win(ai):
                                    game_over = True
                                elif check_draw():
                                    game_over = True

                        if game_over:
                            pygame.time.wait(1000)
                            screen.fill(BOARD_COLOR)
                            draw_lines()
                            for r in range(3):
                                for c in range(3):
                                    if board[r][c] != '':
                                        draw_xo(r, c, board[r][c])
                            pygame.display.update()
                            pygame.time.wait(2000)
                            if check_win(player):
                                display_text(f'Player {player} wins!', 100, (255, 255, 255))
                            elif check_win(ai):
                                display_text(f'Player {ai} wins!', 100, (255, 255, 255))
                            else:
                                display_text('It\'s a draw!', 100, (255, 255, 255))
                            pygame.display.update()
                            pygame.time.wait(3000)

                            if not play_again_or_exit():
                                pygame.quit()
                                sys.exit()

if __name__ == "__main__":
    main()