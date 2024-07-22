from PIL import Image


def main():
    cover_img = Image.open("qrcode.png").convert("RGB");
    cover_width = cover_img.size[0]
    cover = cover_img.load()

    hidden_text = "Hidden text"
    hidden_bin = textToBinary(hidden_text)
    mergeHiddenWithCover(cover,hidden_bin,cover_width)
    cover_img.save("merged_img.png")


def textToBinary(text):
    text_bin = ""
    for ch in text:
        text_bin +='{0:08b}'.format(ord(ch))

    return text_bin


def format_binary(r,g,b):
    return '{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b)


def mergeHiddenWithCover(cover,hidden_bin,SIZE):
    ind = 0
    
    for row in range(SIZE):
        for col in range(SIZE):
            pixel = cover[row,col]
            r,g,b = pixel
            r_bin,g_bin,b_bin = format_binary(r,g,b)

            r_bin = r_bin[0:7] + hidden_bin[ind]
            if ind+1 >= len(hidden_bin):
                cover[row,col] = (int(r_bin,2),int(g_bin,2),int(b_bin,2))
                return
            g_bin = g_bin[0:7] + hidden_bin[ind+1]
            if ind+2 >= len(hidden_bin):
                cover[row,col] = (int(r_bin,2),int(g_bin,2),int(b_bin,2))
                return
            b_bin = b_bin[0:7] + hidden_bin[ind+2]
            ind+=3
            cover[row,col] = (int(r_bin,2),int(g_bin,2),int(b_bin,2))

            if ind >= len(hidden_bin):
                return
    

#calling main
if __name__ == "__main__":
    main()

