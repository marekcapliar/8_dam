# riadok = [0 for i in range(8)]
# print(riadok)
# # je mozne to nahradit
# riadok1 = [0]*8
# print(riadok1)
import pprint
from PIL import Image


def check(x:int, y:int) -> bool:
    global sachovnica
    for i in range(len(sachovnica)):
        for j in range(len(sachovnica[0])):
            if i==y or j==x or i+j==y+x or  i-j==y-x:
                if sachovnica[i][j] == 1:
                    return False
    return True


def drticka(dama:int):
    global sachovnica, count
    if dama == 8:
        pprint.pprint(sachovnica)
        print('---------------------------')
        count += 1
        insert_queen(sachovnica)
    else:
        for i in range(len(sachovnica)):
            if check(i, dama):
                sachovnica[dama][i] = 1
                drticka(dama+1)
                sachovnica[dama][i] = 0


def GUI_sachovnica():
    global policko
    img = Image.new(mode = "RGBA", size = (policko*8, policko*8), color = (0, 128, 0, 255))
    pixels = img.load()

    for y in range(img.size[1]-1):
        for x in range(img.size[0]-1):
            if x//100 % 2 == y//100 % 2:
                pixels[x, y] = (255, 255, 255)
    return img


def insert_queen(sachovnica):
    global img, queen, policko, count
    for y in range(len(sachovnica)):
        for x in range(len(sachovnica[0])):
            if sachovnica[y][x] == 1:
                img.paste(queen, (x*policko, y*policko), queen)
    name = str(count) + '.png'
    img.save(name)
    img = GUI_sachovnica()


sachovnica = []
for i in range(8):
    riadok = [0 for j in range(8)]
    sachovnica.append(riadok)

# pprint.pprint(sachovnica)   # vyprintuje s '\n'
count = 0
policko = 100
img = GUI_sachovnica()

queen = Image.open('queen.png')
queen = queen.resize((policko, policko))

drticka(0)
print(count)
