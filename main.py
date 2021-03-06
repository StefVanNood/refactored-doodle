import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE)
pygame.display.set_caption("doodle")

cameraX = 0
cameraY = 0
vel = 5


def vertices(x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b):

    pygame.draw.polygon(win, (r, g, b),
                        (((x1 - z1) + (cameraX / ((z1.__abs__() / 10) + 1)),
                          (y1 - z1) + (cameraY / ((z1.__abs__() / 10) + 1))),
                        ((x2 - z2) + (cameraX / ((z2.__abs__() / 10) + 1)),
                         (y2 - z2) + (cameraY / ((z2.__abs__() / 10) + 1))),
                        ((x3 - z3) + (cameraX / ((z3.__abs__() / 10) + 1)),
                         (y3 - z3) + (cameraY / ((z3.__abs__() / 10) + 1)))))


run = True
while run:
    win.fill((0, 0, 0))
    pygame.time.delay(16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cameraX = cameraX - vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cameraX = cameraX + vel
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cameraY = cameraY - vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cameraY = cameraY + vel

    #top
    #if cameraY >= 60:

    #top end
    #bottom
    #if cameraY <= -60:

    #bottom end
    #left
    #if cameraX >= 60:

    #left end
    #right
    if cameraX <= -35:
        vertices(300, 100, 0, 300, 100, 20, 300, 300, 0, 255, 0, 0)
        vertices(300, 300, 0, 300, 100, 20, 300, 300, 20, 0, 0, 255)
    #right end
    #front
    vertices(100, 100, 0, 300, 100, 0, 100, 300, 0, 255, 0, 0)
    vertices(100, 300, 0, 300, 100, 0, 300, 300, 0, 0, 0, 255)
    #front end

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("done")
