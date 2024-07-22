from PIL import Image

#main function
def main():
    merged_img = Image.open("merged_img.png")
    decoded_msg = decode(merged_img)
    print(decoded_msg)


#extracting the hidden image from the merged image
def decode(merged_img):
    size = merged_img.size[0]
    merged = merged_img.load()
    hidden_bin = getHiddenBinary(merged,88,size)
    hidden_text = textFromBinary(hidden_bin)
    return hidden_text


#extracting the binary for the hidden image
def getHiddenBinary(merged_img,length,size):
    hidden_bin = ""
    ind = 0

    for row in range(size):
        for col in range(size):
            pixel = merged_img[row,col]
            r,g,b = pixel
            r_bin, g_bin, b_bin = format_binary(r,g,b)
            hidden_bin+= r_bin[-1]
            ind+=1
            if ind >= length:
                return hidden_bin

            hidden_bin+=g_bin[-1]
            ind+=1
            if ind >= length:
                return hidden_bin

            hidden_bin+= b_bin[-1]
            ind+=1
            if ind >= length:
                return hidden_bin
    return hidden_bin

def format_binary(r,g,b):
    return '{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b)


#creating text from binary
def textFromBinary(text_bin):
    hidden_text = ""

    ind = 0

    while ind < len(text_bin):
        hidden_text += chr(int(text_bin[ind:ind+8],2))
        ind+=8

    return hidden_text


#calling main function
if __name__ == "__main__":
    main()
