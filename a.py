from PIL import Image
zagiFile = Image.open('zagiflower1.png')
#create transparent image
canvas = Image.new('RGBA', (6000,3000), (255,255,255,0))
hr1 = (72*3+1,716*3+1)
hr2 = (360*3+1, 889*3+1)
zagi = (1830*3, 952*3)

#go through each pixel of zagiFile
for x in range(zagiFile.width):
    for y in range(zagiFile.height):
        #get pixel value
        pix = zagiFile.getpixel((x,y))
        #if pixel is not transparent
        if pix != (255,255,255,0):
            #draw pixel on canvas
            canvas.putpixel((x*3+zagi[0]-2,y*3+zagi[1]-2), pix)
canvas.save("canvas.png")
