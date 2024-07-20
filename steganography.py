from PIL import Image

WIDTH = 264
HEIGHT = 264


def main():
    cover_img = Image.open("qrcode.png").convert("RGB");
    hidden_img = Image.open("hidden.png")
    merged_img = encode(cover_img,hidden_img)
    merged_img.save("merged_img.png")


def encode(cover_img,hidden_img):
    cover = cover_img.load() #loading into memory
    hidden = hidden_img.load()

    hidden_bin = convertToBinary(hidden)
    mergeHiddenWithCover(cover,hidden_bin)

    return cover_img


def convertToBinary(hidden):
    img_pixels = ""

    for row in range(WIDTH//2):
        for col in range(HEIGHT//2):
            pixel = hidden[row,col]
            r,g,b = pixel
            r_bin, g_bin, b_bin = format_binary(r,g,b)
            img_pixels += r_bin + g_bin + b_bin


    return img_pixels

def format_binary(r,g,b):
    return '{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b)


def mergeHiddenWithCover(cover,hidden_bin):
    ind = 0

    for row in range(WIDTH):
        for col in range(HEIGHT):
            pixel = cover[row,col]
            r,g,b = pixel
            r_bin,g_bin,b_bin = format_binary(r,g,b)
            r_bin = r_bin[0:4] + hidden_bin[ind:ind+4]
            g_bin = g_bin[0:4] + hidden_bin[ind+4:ind+8]
            b_bin = b_bin[0:4] + hidden_bin[ind+8:ind+12]
            ind+=12
            cover[row,col] = (int(r_bin,2),int(g_bin,2),int(b_bin,2))

            if ind >= len(hidden_bin):
                return
    

#calling main
if __name__ == "__main__":
    main()

