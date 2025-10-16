# Example file showing a circle moving on screen
import pygame
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FONT = pygame.font.SysFont('consolas', 18)
dt = 0
speed = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
posb = pygame.Vector2(0,0)
scr_ymax = (screen.get_height())
scr_xmax = (screen.get_width())
pos = 0
angle = 0
ground = 0
spstr = ""
thru = 0
thru_timer = 0
gravity = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    pos = pos + speed * dt
    if keys[pygame.K_w]:
        speed += 0.5
        if keys[pygame.K_w] and ground == 1:
            # give an immediate jump impulse (negative to go up)
            player_pos.y = scr_ymax - 50
            ground = 0
    elif keys[pygame.K_s] and speed > 0:
        speed -= 0.5
    if keys[pygame.K_w] and ground == 1:
        speed = -1  # jump impulse
        ground = 1
    if player_pos.y >= scr_ymax - 40:
        player_pos.y = scr_ymax - 40
        speed = 0
        ground = 1
    else:
        ground = 0
    if keys[pygame.K_a]:
        angle -= 4
    if keys[pygame.K_d]:
        angle += 4
    rad_ang = math.radians(angle) # maths to turn deg into direct radians or smthn
    posb.x = speed * math.sin(rad_ang) # sin
    posb.y = -speed * math.cos(rad_ang) # cos
    posb.y -= gravity
    if ground == 0:
            gravity -= 0.05  # gravity
    #psl; if posb.y over 15; gravity = 0
    if posb.y >= 15:
        gravity = 0
    player_pos += posb
    # flip() the display to put your work on screen
    if keys[pygame.K_r]:
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        speed = 0
    if player_pos.x <= 0 and thru == 0:
        player_pos.x = scr_xmax
        print("go")
        thru = 1
    if player_pos.x >= scr_xmax - 0 and thru == 0:
        player_pos.x = 0
        thru = 1
    if thru_timer >= 0.2:
        thru_timer = 0
        thru = 0
    thru_timer += dt
    if speed >= 29.5:
        speed = 29.5
    spstr = f"Speed: {speed:.2f}"
    speed_disp = FONT.render(spstr, True, (255,255,255))
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    print(thru_timer, " : ", thru)
    screen.blit(speed_disp, (80,300))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit() 