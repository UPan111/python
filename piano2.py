import pygame, sys
def get_key_index(key,kList):
    for i in range(len(kList)):
        if key == ord(kList[i]):
            return i
    return -1
#======pygame init=======
pygame.init()
pianoImg = pygame.image.load('piano.bmp')#读入背景图片
screen = pygame.display.set_mode(pianoImg.get_size())#产生窗口对象
pygame.display.set_caption('RT-PIANO')#窗口命名
#---------data init---------
noteImg = pygame.image.load('note.bmp')#add in V1.1
keyList = 'asdfghj'+'qwertyu'+'1234567'
soundList = [] #与keyList是一一对应关系，按键到声音文件
for noteLevel in '345':
    for noteName in 'cdefgab':
        oggsound = pygame.mixer.Sound(noteName + noteLevel + '.ogg')
        soundList.append(oggsound)
keyFlagList = [0] * len(keyList)#初始化音符标记，记录每个建是否被按下
while True: #----------main loop-------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            i = get_key_index(event.key, keyList)#获取音符编号
            if i >= 0:
                soundList[i].play()#演奏
                keyFlagList[i] = 1#显示标记
        elif event.type == pygame.KEYUP:#松开建模去音符
            i = get_key_index(event.key, keyList)#获取音符编号
            if i >= 0:
                keyFlagList[i] = 0
    screen.blit(pianoImg,(0,0))#先画钢琴背景
    for i in range(len(keyFlagList)):#再画音符
        if keyFlagList[i]:
            screen.blit(noteImg,(i * 30 + 2, 80))
    pygame.display.update() #屏幕刷新
