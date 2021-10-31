import pygame, sys
pygame.init()
pianoImg = pygame.image.load('piano.bmp')
screen = pygame.display.set_mode(pianoImg.get_size())
pygame.display.set_caption('RT-Piano')
#中音
Do = pygame.mixer.Sound('c4.ogg')
Re = pygame.mixer.Sound('d4.ogg')
Mi = pygame.mixer.Sound('e4.ogg')
Fa = pygame.mixer.Sound('f4.ogg')
So = pygame.mixer.Sound('g4.ogg')
La = pygame.mixer.Sound('a4.ogg')
Si = pygame.mixer.Sound('b4.ogg')
#高音
hDo = pygame.mixer.Sound('c5.ogg')
hRe = pygame.mixer.Sound('d5.ogg')
hMi = pygame.mixer.Sound('e5.ogg')
hFa = pygame.mixer.Sound('f5.ogg')
hSo = pygame.mixer.Sound('g5.ogg')
hLa = pygame.mixer.Sound('a5.ogg')
hSi = pygame.mixer.Sound('b5.ogg')
#低音
lDo = pygame.mixer.Sound('c3.ogg')
lRe = pygame.mixer.Sound('d3.ogg')
lMi = pygame.mixer.Sound('e3.ogg')
lFa = pygame.mixer.Sound('f3.ogg')
lSo = pygame.mixer.Sound('g3.ogg')
lLa = pygame.mixer.Sound('a3.ogg')
lSi = pygame.mixer.Sound('b3.ogg')
#超低
hlDo = pygame.mixer.Sound('c2.ogg')
hlRe = pygame.mixer.Sound('d2.ogg')
hlMi = pygame.mixer.Sound('e2.ogg')
hlFa = pygame.mixer.Sound('f2.ogg')
hlSo = pygame.mixer.Sound('g2.ogg')
hlLa = pygame.mixer.Sound('a2.ogg')
hlSi = pygame.mixer.Sound('b2.ogg')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #zhong
            if event.key == ord('q'):
                Do.play()
            if event.key == ord('w'):
                Re.play()
            if event.key == ord('e'):
                Mi.play()
            if event.key == ord('r'):
                Fa.play()
            if event.key == ord('t'):
                So.play()
            if event.key == ord('y'):
                La.play()
            if event.key == ord('u'):
                Si.play()
            #gao
            if event.key == ord('1'):
                hDo.play()
            if event.key == ord('2'):
                hRe.play()
            if event.key == ord('3'):
                hMi.play()
            if event.key == ord('4'):
                hFa.play()
            if event.key == ord('5'):
                hSo.play()
            if event.key == ord('6'):
                hLa.play()
            if event.key == ord('7'):
                hSi.play()
            #di
            if event.key == ord('a'):
                lDo.play()
            if event.key == ord('s'):
                lRe.play()
            if event.key == ord('d'):
                lMi.play()
            if event.key == ord('f'):
                lFa.play()
            if event.key == ord('g'):
                lSo.play()
            if event.key == ord('h'):
                lLa.play()
            if event.key == ord('j'):
                lSi.play()
            #zdi
            if event.key == ord('z'):
                hlDo.play()
            if event.key == ord('x'):
                hlRe.play()
            if event.key == ord('c'):
                hlMi.play()
            if event.key == ord('v'):
                hlFa.play()
            if event.key == ord('b'):
                hlSo.play()
            if event.key == ord('n'):
                hlLa.play()
            if event.key == ord('m'):
                hlSi.play()
    screen.blit(pianoImg, (0, 0))
    pygame.display.update()
