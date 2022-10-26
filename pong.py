"""
Pong Game
"""

import pygame
from pygame.locals import *
pygame.init()

# Setting up Display
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

# Caption
caption = "Ping-Pong Game"
pygame.display.set_caption(caption)

# Frame Rate
FPS = 60

# Colors
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
CYAN = (0, 255, 255)
GREEN = (0,255,0)

# Sprite Dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 20,100
BALL_RADIUS = 7

# Misc.
FONT = pygame.font.SysFont('firacode', 50)
WINNER_SCORE = 10



class Paddle:
    COLOR = CYAN
    VEL_VECTOR = 4
    
    
    def __init__(self, x, y, width, height) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width  = width
        self.height = height
        
        
    def draw(self, window):
        pygame.draw.rect(
            window, self.COLOR, (self.x, self.y, self.width, self.height))
        
        
    def move(self, up=True):
        if up : 
            self.y = self.y - self.VEL_VECTOR       
        else : 
            self.y = self.y + self.VEL_VECTOR       


    def reset(self):
        self.x = self.original_x 
        self.y = self.original_y 
        


class Ball:
    VEL_MAX = 5
    COLOR = GREEN
    
    
    def __init__(self, x, y, radius) -> None:
         self.x = self.orginal_x = x
         self.y = self.orginal_y = y
         self.radius = radius
         self.x_vel_vect = self.VEL_MAX
         self.y_vel_vect = 0
         
    
    def draw(self, window) -> None:
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)
        
    
    def move(self):
        self.x = self.x + self.x_vel_vect
        self.y = self.y + self.y_vel_vect
    
    
    def reset(self) -> None:
        self.x = self.orginal_x
        self.y = self.orginal_y
        self.y_vel_vect = 0
        self.x_vel_vect *= -1
    
    
    
def draw(window, paddles, ball, l_score, r_score):
    window.fill(BLACK)
    
    l_score_text = FONT.render(f"X : {l_score}", 1, WHITE)
    r_score_text = FONT.render(f"Y : {r_score}", 1, WHITE)
    window.blit(l_score_text, (WIDTH//4 - l_score_text.get_width()//2, 20))
    window.blit(r_score_text, (WIDTH * (3/4) - r_score_text.get_width()//2, 20))
    
    for paddle in paddles:
        paddle.draw(window)
        
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))
        
    ball.draw(window)
        
    pygame.display.update()
   
   
    
    
def collision(ball, l_paddle, r_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel_vect *= -1
        
    elif ball.y - ball.radius <= 0:
        ball.y_vel_vect *= -1


    if ball.x_vel_vect < 0:
        if ball.y >= l_paddle.y and ball.y <= l_paddle.y + l_paddle.height:
            if ball.x - ball.radius <= l_paddle.x + l_paddle.width:
                ball.x_vel_vect *= -1
                
                middle_y = l_paddle.y + l_paddle.height/2
                difference_y = middle_y - ball.y
                reduction_factor = (l_paddle.height / 2) / ball.VEL_MAX
                y_vel_vect = difference_y / reduction_factor
                ball.y_vel_vect = -1 * y_vel_vect          
    
    else:
        if ball.y >= r_paddle.y and ball.y <= r_paddle.y + r_paddle.height:
            if ball.x + ball.radius >= r_paddle.x:
                ball.x_vel_vect *= -1
                
                middle_y = r_paddle.y + r_paddle.height/2
                difference_y = middle_y - ball.y 
                reduction_factor = (r_paddle.height / 2) / ball.VEL_MAX
                y_vel_vect = difference_y / reduction_factor
                ball.y_vel_vect = -1 * y_vel_vect          

    
    
    
def paddle_movement(keys, l_paddle, r_paddle):
    if keys[pygame.K_w] and l_paddle.y - l_paddle.VEL_VECTOR >= 0:
            l_paddle.move(up=True)
            
    if keys[pygame.K_s] and l_paddle.y + l_paddle.VEL_VECTOR + l_paddle.height <= HEIGHT:
            l_paddle.move(up=False)
            
        
    if keys[pygame.K_UP] and r_paddle.y - r_paddle.VEL_VECTOR >= 0:
            r_paddle.move(up=True)
            
    if keys[pygame.K_DOWN] and r_paddle.y + r_paddle.VEL_VECTOR + r_paddle.height <= HEIGHT:
            r_paddle.move(up=False)
        
    


def main():
    running = True
    clock = pygame.time.Clock()     # Regulating Pace of code
    
    l_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    r_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
    
    l_score = r_score = 0
    
    # main loop
    while running:
        clock.tick(FPS)         #Program will update @60 FPS max
        draw(WINDOW, [l_paddle, r_paddle], ball, l_score, r_score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            
        keys = pygame.key.get_pressed()    
        paddle_movement(keys, l_paddle, r_paddle)
        
        ball.move()
        collision(ball, l_paddle, r_paddle)
        
        if ball.x < 0:
            r_score = r_score + 1
            ball.reset()
        elif ball.x > WIDTH:
            l_score = l_score + 1
            ball.reset()
        
        
        over = False
        if l_score >= WINNER_SCORE:
            over = True
            final_win = "X won the Game !! \n Restarting..."
        elif r_score >= WINNER_SCORE:
            over = True
            final_win = "Y won the Game !! \n Restarting..."
        
        
        if over:
            text_obj = FONT.render(final_win, 1, WHITE)
            WINDOW.blit(text_obj, (WIDTH//2 - text_obj.get_width()//2, HEIGHT//2 - text_obj.get_height()//2))
            
            pygame.display.update()
            pygame.time.delay(5000)
            
            ball.reset()
            l_paddle.reset()
            r_paddle.reset()
            
            l_score = 0
            r_score = 0
        
    pygame.quit()
    


# Start the Execution of the Program
if __name__ == "__main__":
    main()