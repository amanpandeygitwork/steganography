from PIL import Image

#SOME GLOBAL VARIABLES
WIDTH = 264
HEIGHT = 264

#main function
def main():
    merged_img = Image.open("merged_img.png")
    decoded_img = decode(merged_img)
    decoded_img.save("decoded.png")


#extracting the hidden image from the merged image
def decode(merged_img):
    pixel_count = 132*132
    loaded_merged_img = merged_img.load()
    hidden_bin = extract_hidden(loaded_merged_img,pixel_count)
    hidden_img = createImageFromBinary(hidden_bin)
    return hidden_img


#extracting the binary for the hidden image
def extract_hidden(merged_img,pixel_count):
    hidden_bin = ""
    ind = 0

    for row in range(WIDTH):
        for col in range(HEIGHT):
            pixel = merged_img[row,col]
            r,g,b = pixel
            r_bin, g_bin, b_bin = format_binary(r,g,b)
            hidden_bin+= r_bin[4:8] + g_bin[4:8] + b_bin[4:8]
            ind+=1
            if ind >= pixel_count * 2:
                return hidden_bin
        
    return hidden_bin

def format_binary(r,g,b):
    return '{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b)


#creating the hidden image back from it's binary
def createImageFromBinary(hidden_bin):
    hidden_img = Image.new("RGB",(WIDTH//2,HEIGHT//2))
    loaded_hidden_img = hidden_img.load()

    ind = 0

    for row in range(WIDTH//2):
        for col in range(HEIGHT//2):
            r_bin = hidden_bin[ind:ind+8]
            g_bin = hidden_bin[ind+8:ind+16]
            b_bin = hidden_bin[ind+16:ind+24]

            loaded_hidden_img[row,col] = (int(r_bin,2),int(g_bin,2),int(b_bin,2))
            ind+=24

    return hidden_img


#calling main function
if __name__ == "__main__":
    main()
