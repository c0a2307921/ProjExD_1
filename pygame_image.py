import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img3 = pg.image.load("fig/pg_bg.jpg")
    bg_img4 = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    tmr=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%1600)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1599, 0])
        screen.blit(bg_img3, [x+3199, 0])
        screen.blit(bg_img4, [x+4799, 0])
        screen.blit(kk_img, [300, 200]) 
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()