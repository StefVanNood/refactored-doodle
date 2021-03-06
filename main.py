import pygame
pygame.init()

x_screen = 500
y_screen = 500

win = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE)
pygame.display.set_caption("doodle")

cameraX = 0
cameraY = 0
vel = 5

object1 = []
row = []
i = 1
f = open("cube").read()
for Value in f.split():
    row.append(int(Value))
    if i == 10:
        object1.append(row)
        row = []
        i = 0
    i = i + 1
print(object1[0])
print(len(object1))

object2 = []
row = []
i = 1
f = open("pyramid").read()
for Value in f.split():
    row.append(int(Value))
    if i == 10:
        object2.append(row)
        row = []
        i = 0
    i = i + 1
print(object2[0])
print(len(object2))


def vertices(x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b, x, y):
    surface = pygame.display.get_surface()
    x_width, y_width = surface.get_width(), surface.get_height()
    z_speed = 200
    if (cameraX / ((z1.__abs__() / 100) + 1)).__abs__() >= z1 and \
            not z1 == 1:
        z_speed = z1
    if (cameraY / ((z1.__abs__() / 100) + 1)).__abs__() >= z1 and \
            not z1 == 1:
        z_speed = z1
    if (cameraX / ((z2.__abs__() / 100) + 1)).__abs__() >= z2 and \
            not z2 == 1:
        z_speed = z2
    if (cameraY / ((z2.__abs__() / 100) + 1)).__abs__() >= z2 and \
            not z2 == 1:
        z_speed = z2
    if (cameraX / ((z3.__abs__() / 100) + 1)).__abs__() >= z3 and \
            not z3 == 1:
        z_speed = z3
    if (cameraY / ((z3.__abs__() / 100) + 1)).__abs__() >= z3 and \
            not z3 == 1:
        z_speed = z3

    pygame.draw.polygon(win, (r, g, b),
                        (
                        ((x1 + x_width / 2 - 200 + x) + (cameraX / ((z1.__abs__() / z_speed) + 1)),
                         (y1 + y_width / 2 - 200 + y) + (cameraY / ((z1.__abs__() / z_speed) + 1))),
                        ((x2 + x_width / 2 - 200 + x) + (cameraX / ((z2.__abs__() / z_speed) + 1)),
                         (y2 + y_width / 2 - 200 + y) + (cameraY / ((z2.__abs__() / z_speed) + 1))),
                        ((x3 + x_width / 2 - 200 + x) + (cameraX / ((z3.__abs__() / z_speed) + 1)),
                         (y3 + y_width / 2 - 200 + y) + (cameraY / ((z3.__abs__() / z_speed) + 1)))
                        ))


def render_object(color_r, color_g, color_b, location_x, location_y):
    for z in range(len(object1)):
        if object1[z][9] == 5:
            if cameraY >= 40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r, color_g, color_b,
                         location_x, location_y)
        if object1[z][9] == 3:
            if cameraY <= -40:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 100, color_g - 200, color_b - 200,
                         location_x, location_y)
        if object1[z][9] == 2:
            if cameraX >= 35:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 100, color_g - 100, color_b - 100,
                         location_x, location_y)
        if object1[z][9] == 4:
            if cameraX <= -35:
                vertices(object1[z][0], object1[z][1], object1[z][2],
                         object1[z][3], object1[z][4], object1[z][5],
                         object1[z][6], object1[z][7], object1[z][8],
                         color_r - 10, color_g - 10, color_b - 10,
                         location_x, location_y)
        if object1[z][9] == 1:
            vertices(object1[z][0], object1[z][1], object1[z][2],
                     object1[z][3], object1[z][4], object1[z][5],
                     object1[z][6], object1[z][7], object1[z][8],
                     color_r - 50, color_g - 50, color_b - 50,
                     location_x, location_y)


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

    render_object(100, 255, 255, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
print("stopped")
