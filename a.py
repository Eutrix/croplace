from PIL import Image
kravata = Image.open('kravata.png')
k2 = Image.new('RGBA', (200//13, 780//13), (255,255,255,0))
# go through each pixel of a file
for x in range(5,kravata.width,13):
    for y in range(5,kravata.height,13):
        #get pixel value
        pix = kravata.getpixel((x,y))
        k2.putpixel((x//13,y//13), pix)
k2.save('kravata-resized.png')

