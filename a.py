from PIL import Image
file = Image.open('golubica-big.png')

scale = 16

new = Image.new('RGBA', (file.width//scale+1, file.height//scale+1), (255,255,255,0))
# go through each pixel of a file
for x in range(6,file.width,scale):
    for y in range(6,file.height,scale):
        #get pixel value
        pix = file.getpixel((x,y))
        new.putpixel(((x-6)//scale,(y-6)//scale), pix)
new.save('golubica-resized.png')

