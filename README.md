# Steganography
Hidding an image behind another by replacing LSB of the cover image "qrcode.png" by the bit values of another image "hidden.png"
Using a hidden image that is half the size of the cover image allows us to save any information loss on the hidden image

## Create a copy of the project
```bash
git clone https://github.com/amanpandeygitwork/steganography.git
```

## First we generate a qr code image
```bash
python generate_qr.py
```
After you enter an input string in this case I am using google.com a new qrcode will be generated like one below
![qrcode](qrcode.png?raw=true)

### Scanning the qr online
![qrcode](./assets/scanning_qr.png?raw=true) 

## Merging the "hidden.png" image with cover "qrcode.png"
![qrcode](hidden.png?raw=true) 
```bash
python steganography.py
```
This should hide the image "hidden.png" within "qrcode.png" and generate a new image "merged_img.png" 
![qrcode](merged_img.png?raw=true) 

Even though it looks the same as "qrcode.png" a quick comparision of the two would show otherwise
![qrcode](./assets/absolute_error.png?raw=true) 

## Finally scanning "the merged_img.png" seems to work too
![qrcode](./assets/merged_img_qr_scan.png?raw=true) 

## To decode the hidden image back run the following script
```bash
python reconstruct.py
```

This will generate a new image "decoded.png" which is the hidden image
