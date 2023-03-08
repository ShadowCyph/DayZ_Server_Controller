import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load("Assets\\notifications\\click.wav")
class button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height*scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.hovering = False

    def draw(self,image,image_hover,surface):
        win = surface
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.hovering = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.mixer.music.play()
        else:
            self.hovering = False
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if self.hovering == True:
            self.image = image_hover
        if self.hovering == False:
            self.image = image

        win.blit(self.image, (self.rect.x, self.rect.y))

        return action