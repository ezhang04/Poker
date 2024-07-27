import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clientNumber = 0

class Player ():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        val = 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= val
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += val
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= val
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += val
        self.rect = (self.x, self.y, self.width, self.height)

def redraw(win, player):
    window.fill((255, 255, 255))
    clock = pygame.time.Clock()
    clock.tick(60)
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    player = Player(50, 50, 100, 100, (0, 255, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw(window, player)

main()
                