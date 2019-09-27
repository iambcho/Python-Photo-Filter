from PIL import Image

def grayscale(ogimg):
    ogpix = ogimg.load()
    for x in range(ogimg.size[0]):
        for y in range(ogimg.size[1]):
            average = sum(ogpix[x,y])//3
            ogpix[x,y] = (average,)*3
    return ogimg



def flip(ogimg):
    width, height = ogimg.size
    newimg = Image.new('RGB', (height, width))

    pix = newimg.load()
    ogpix = ogimg.load()
    for x in range(height):
        for y in range(width):
            new_x = y
            new_y = height - x - 1
            t = new_x, new_y
            pix[x, y] = ogpix[t]
    return newimg



def pixelate(ogimg):
    width, height = ogimg.size
    newimg = Image.new('RGB', (width, height))
    pix = newimg.load()
    ogpix = ogimg.load()

    for x in range(0, width-(width%20), 20):
        for y in range(0, height-(height%20)):
            for size in range(0, 20):

                pix[x+size, y] = ogpix[x, y]
                # pix[x, y] = ogpix[x, y]

    return newimg




def scaledown(ogimg, newimg, startx, starty):
    width, height = ogimg.size
    maxwidth = width//2
    maxheight = height//2

    newimg = Image.new('RGB', (maxwidth, maxheight))
    pix = newimg.load()
    ogpix = ogimg.load()

    ratio = min(maxwidth/width, maxheight/height)

    for x in range(maxwidth):
        for y in range(maxheight):
            pix[x, y] = ogpix[x//ratio, y// ratio]

    return newimg



def mirror(ogimg, newimg):
    width, height = ogimg.size;
    newpix = newimg.load()
    ogpix = ogimg.load()

    #Creates image at top left
    for x in range(width):
        for y in range(height):
            newx, newy = x, height - y - 1
            newpix[x, y] = ogpix[newx, newy]

    #creates image at bottom left
    for x in range(width):
        for y in range(height):
            newpix[x, y+height] = ogpix[x, y]

    #creates image at top left
    for x in range(width):
        for y in range(height):
            newx, newy = width - x - 1, height - y - 1
            newpix[x+width, y] = ogpix[newx, newy]

    #creates image at bottom left
    for x in range(width):
        for y in range(height):
            newx, newy = width - x - 1, y
            newpix[x+width, y+height] = ogpix[newx, newy]
    return newimg


def tetris_filter(orig_img):
    width, height = orig_img.size
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = orig_img.load()

    for x in range(0, width-(width%30), 30):
        for y in range(0, height-(height%30), 30):
            for size in range(0, 30):

                pixels[x+size, y] = orig_pixels[x, y]
                pixels[x, y+size] = orig_pixels[x, y]

    return img

if __name__ == "__main__":
    img = Image.open('wallaby.jpg')
    grayscale(img).show()
    flip(img).show()
    pixelate(img).show()
    tetris_filter(img).show()

