import pygame
sheet_w=500
sheet_h=700
sheet=pygame.display.set_mode((sheet_w,sheet_h))

def text_objects(text,font,color):
    textSurface = font.render(text, True , color)
    return textSurface, textSurface.get_rect()
def message_display(text,x,y,color,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(str(text),largeText,color)
    TextRect.center = ((x),(y))
    sheet.blit(TextSurf,TextRect)
    pygame.display.update()