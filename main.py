import PIL
from PIL import Image

img = Image.new(mode='RGB', size=(4096,4096))
pixels=img.load()
for i in range(1, 4097):
    for j in range(1, 4097):
        for r in range(0,256):
            for g in range(0,256):
                for b in range(0, 256):
                    pixels[i,j]=(r,g,b)
                    print(i)
                    print(j)
                    print(r)
                    print(g)
                    print(b)
                    print('-'*50)
                    img.save('im.png')
