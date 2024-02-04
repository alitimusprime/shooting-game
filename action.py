import pygame
import random
import time

pygame.font.init()

# height width aur color  
screen_height = 600
screen_width = 800
screen_title = "Shera"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_title)

background = pygame.image.load("BG.jpg")
background_color = (255, 255, 255)

speed = 5

line_color = (255, 255, 255)
line_thickness = 4

bullet_width= 15
bullet_height = 15
bullet_vel = 8

player_1_image = pygame.image.load("ch1.png")
player_2_image = pygame.image.load("smoker.png")

player_1_image_width = 80
player_1_image_height = 80

player_2_image_width = 80
player_2_image_height = 80

red = (255, 0, 0)
green = (0, 255, 0)

player_1_image = pygame.transform.scale (player_1_image, (player_1_image_width, player_1_image_height))

player_2_image = pygame.transform.scale (player_2_image, (player_2_image_width, player_2_image_height))

player1 = pygame.Rect(105, 500, player_1_image_width, player_1_image_height)

player2 = pygame.Rect(650, 500, player_2_image_width, player_2_image_height)

player1_bullet = []
player2_bullet = []

player1_health = 200
player2_health = 200

player_1_image_rect = player_1_image.get_rect()
player_1_image_rect.x = 95
player_1_image_rect.y = 538

player_2_image_rect = player_2_image.get_rect()
player_2_image_rect.x = 680
player_2_image_rect.y = 500

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

pygame.display.flip()

clock = pygame.time.Clock()

#running variable
running = True

def bullet_move(player1_bullet, player2_bullet):
    for bullet in player1_bullet:
        bullet.x += bullet_vel
        if bullet.x > screen_width:
            player1_bullet.remove(bullet)
    
    for bullet in player2_bullet:
        bullet.x -= bullet_vel
        if bullet.x < 0:
            player2_bullet.remove(bullet)
            


def draw(player1, player2, player1_bullet, player2_bullet):

   
    screen.fill(background_color)

    screen.blit(pygame.transform.scale(background, (screen_width, screen_height)), (0, 0))

    screen.blit(player_1_image, (player1.x, player1.y))
    
    screen.blit(player_2_image, (player2.x, player2.y))
    
    pygame.draw.line(screen, line_color, (screen_width/2,0), (screen_width/2, screen_height), line_thickness)

    for bullet in player1_bullet:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        if pygame.Rect.colliderect(bullet, player2):
            player1_bullet.remove(bullet)

        


    for bullet in player2_bullet:
        pygame.draw.rect(screen, (0, 0, 0), bullet)
        if pygame.Rect.colliderect(bullet, player1):
            player2_bullet.remove(bullet)

    bullet_move(player1_bullet, player2_bullet)        

def keys_player1():
    keys = pygame.key.get_pressed()
    if keys [pygame.K_a]: 
        player1.x -= speed
        if player1.x < 0:
            player1.x = 0
        
    elif keys [pygame.K_d]:
        player1.x += speed 
        if player1.x > screen_width/2 - 80:
            player1.x = 320
                
    elif keys [pygame.K_w]:
        player1.y -= speed
        if player1.y < 0:
            player1.y = 0


    elif keys [pygame.K_s]:
        player1.y += speed 
        if player1.y > screen_height - player_1_image_height:
            player1.y = 520
            
        
    
def keys_player2():

    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_LEFT]:
         player2.x -= speed 
         if player2.x < screen_width/2 :
             player2.x = 400
       
    
    elif keys [pygame.K_RIGHT]:
        player2.x += speed 
        if player2.x > screen_width - player_2_image_width:
            player2.x = screen_width - player_2_image_width
       


    elif keys [pygame.K_UP]:
        player2.y -= speed
        if player2.y < 0:
            player2.y = 0
        
        
    elif keys [pygame.K_DOWN]:
        player2.y += speed 
        if player2.y > screen_height - player_2_image_height:
            player2.y = screen_height - player_2_image_height



def health1(current_health):
    pygame.draw.rect(screen, red, (595, 10, 200, 10))
    pygame.draw.rect(screen, green, (595, 10, current_health, 10))
    for bullet in player1_bullet:
        if bullet.colliderect(player2):
            current_health -= 20
            pygame.display.flip()
    return current_health

def health2(current_health):
    pygame.draw.rect(screen, red, (5, 10, 200, 10))
    pygame.draw.rect(screen, green, (5, 10, current_health, 10))
    for bullet in player2_bullet:
        if bullet.colliderect(player1):
            current_health -= 20
    pygame.display.flip()
    return current_health



while running:

    keys_player1()

    keys_player2()

    for event in pygame.event.get():   

        key = pygame.key.get_pressed()   
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_c:

                bullet = pygame.Rect (player1.x + player_1_image_width, player1.y + player_1_image_height//2, bullet_width, bullet_height)
                player1_bullet.append(bullet)
                
            
            if event.key == pygame.K_RCTRL:
                bullet = pygame.Rect (player2.x , player2.y + player_1_image_height//2 , bullet_width, bullet_height)
                player2_bullet.append(bullet)
        
    player1_health = health1(player1_health)

    player2_health = health2(player2_health)

    #game bund karna health khatam hone ke baad

    if player2_health <= 0:
        winner_text = font.render("Player 2 Wins!", True, text_color)
        screen.blit(winner_text, (screen_width // 2 - 100, screen_height // 2))
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False
    
    if player1_health <= 0:
        winner_text = font.render("Player 1 Wins!", True, text_color)
        screen.blit(winner_text, (screen_width // 2 - 100, screen_height // 2))
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False


                
    draw(player1, player2, player1_bullet, player2_bullet)

    clock.tick(120)

   
pygame.quit()
