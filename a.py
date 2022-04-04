from PIL import Image
modric = Image.open('modric4.png')
m2 = Image.new('RGBA', (modric.width//12+1, modric.height//12+1), (255,255,255,0))
# go through each pixel of a file
for x in range(6,modric.width,12):
    for y in range(6,modric.height,12):
        #get pixel value
        pix = modric.getpixel((x,y))
        m2.putpixel(((x-6)//12,(y-6)//12), pix)
m2.save('modric-resized.png')

