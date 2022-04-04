from PIL import Image

reddit_colors = {"6d001a", "be0039", "ff4500", "ffa800", "ffd635", "fff8b8", "00a368", "00cc78", "7eed56", "00756f", "009eaa", "00ccc0", "2450a4", "3690ea", "51e9f4", "493ac1", "6a5cff", "94b3ff", "811e9f", "b44ac0", "e4abff", "de107f", "ff3881", "ff99aa", "6d482f", "9c6926", "ffb470", "000000", "515252", "898d90", "d4d7d9", "ffffff"}
reddit_colors = set([tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) for h in reddit_colors])

def closest_color(r, g, b):
    color_diffs = []
    for color in reddit_colors:
        cr, cg, cb = color
        color_diff = (r - cr)**2 + (g - cg)**2 + (b - cb)**2
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

hr1 = ((73*3,717*3), Image.open('hr1.png'))
hr2 = ((361*3, 890*3), Image.open('hr2.png'))
zagi = ((1830*3, 952*3), Image.open('zagiflower1.png'))
kravata = ((434*3,912*3), Image.open('kravata2.png'))
modric = ((330*3, 1088*3), Image.open('modric-resized-edited.png'))

canvas = Image.new('RGBA', (6000,6000), (255,255,255,0))

for i in [hr1, hr2, zagi, kravata, modric]:
    x0, y0 = i[0]
    file = i[1]
    #go through each pixel of a file
    for x in range(file.width):
        for y in range(file.height):
            #get pixel value
            pix = file.getpixel((x,y))
            #if pixel is not transparent
            if pix != (255,255,255,0):
                #draw pixel on canvas
                canvas.putpixel((x*3+x0-2,y*3+y0-2), closest_color(pix[0], pix[1], pix[2]) + (pix[3],))

canvas.save("canvas.png")
