from PIL import Image
zagiFile = Image.open('zagiflower1.png')
hr1File = Image.open('hr1.png')
hr2File = Image.open('hr2.png')
#create transparent image
canvas = Image.new('RGBA', (6000,3000), (255,255,255,0))
hr1 = (73*3,717*3)
hr2 = (361*3, 890*3)
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

#go through each pixel of hr1
for x in range(hr1File.width):
    for y in range(hr1File.height):
        #get pixel value
        pix = hr1File.getpixel((x,y))
        #if pixel is not transparent
        if pix != (255,255,255,0):
            #draw pixel on canvas
            canvas.putpixel((x*3+hr1[0]-2,y*3+hr1[1]-2), pix)

#go through each pixel of hr2
for x in range(hr2File.width):
    for y in range(hr2File.height):
        #get pixel value
        pix = hr2File.getpixel((x,y))
        #if pixel is not transparent
        if pix != (255,255,255,0):
            #draw pixel on canvas
            canvas.putpixel((x*3+hr2[0]-2,y*3+hr2[1]-2), pix)
canvas.save("canvas.png")
