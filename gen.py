from PIL import Image

zagiFile = Image.open('zagiflower1.png')
hr1File = Image.open('hr1.png')
hr2File = Image.open('hr2.png')

hr1 = ((73*3,717*3), hr1File)
hr2 = ((361*3, 890*3), hr2File)
zagi = ((1830*3, 952*3), zagiFile)

#create transparent image
canvas = Image.new('RGBA', (6000,3000), (255,255,255,0))

for i in [hr1, hr2, zagi]:
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
                canvas.putpixel((x*3+x0-2,y*3+y0-2), pix)

canvas.save("canvas.png")
