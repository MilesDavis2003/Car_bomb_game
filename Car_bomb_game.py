import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
road = pygame.Rect(200, 0, 400, 600)

yellow_div1 = pygame.Rect(390, 210, 20, 100)
yellow_div2 = pygame.Rect(390, 450, 20, 100)
yellow_div3 = pygame.Rect(390, 0, 20, 100)

bomb1 = pygame.image.load('Bomb(1).png')
bomb1 = pygame.transform.scale(bomb1, (50, 50))
bomb_rect = pygame.Rect(200, 50, 50, 50)

race_car = pygame.image.load('red_racer.png')
race_car = pygame.transform.scale(race_car,(200, 100))
race_car = pygame.transform.rotate(race_car, 270)
red_racer = pygame.Rect(300, 350, 100, 200)

clock = pygame.time.Clock()
dividers = [yellow_div1, yellow_div2, yellow_div3]

def game():
    run = True
    count = 0
    fps = 80
    while run:
        count += 1
        text = pygame.font.Font(None, 32)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
        screen.fill('green')
        pygame.draw.rect(screen, (0, 0, 0), road)
        pygame.draw.rect(screen, (255, 255, 0), yellow_div1)
        pygame.draw.rect(screen, (255, 255, 0), yellow_div2)
        pygame.draw.rect(screen, (255, 255, 0), yellow_div3)
        yellow_div()
        #text_surf = text.render('Score: ', True, (255, 255, 255))
        #screen.blit(text_surf, (600, 50))
        screen.blit(bomb1, (bomb_rect.x, bomb_rect.y))
        screen.blit(race_car, (red_racer.x, red_racer.y))
        car_controls()
        obstacle(bomb_rect)
        if red_racer.colliderect(bomb_rect):
            run = False
            print("Game Over")
        pygame.display.update()
        clock.tick(fps)
        if count % 150 == 0:
            fps += 5
        if fps == 250:
            fps = 250
    pygame.quit()

def yellow_div():
    for i in dividers:
        i.y += 5
        if i.y > 600:
            i.y = -100

def car_controls():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and red_racer.x > 200:
        red_racer.x -= 5
    if keys[pygame.K_RIGHT] and red_racer.x < 500:
        red_racer.x += 5
    if keys[pygame.K_UP] and red_racer.y > 0:
        red_racer.y -= 5
    if keys[pygame.K_DOWN] and red_racer.y < 500:
        red_racer.y += 5
def obstacle(bomb_rect):
    for i in range(1):
        bomb_rect.y += 5
        if bomb_rect.y > 600:
            bomb_rect.y = -10
            bomb_rect.x = random.randint(250, 500)
def high_score():
    score = 0
    score += 1
    return score
if __name__ == '__main__':
    game()

