# Steganography
Hiding information within a image


## Changes
- Changed segno with qrcode
- Changed system from hiding image to text
- Uses 1LSB instead of 4LSBs

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

## Merging the text with cover "qrcode.png"
"Hidden text"
```bash
python steganography.py
```
This will hide the text "Hidden text" within "qrcode.png" and generate a new image "merged_img.png" 
![qrcode](merged_img.png?raw=true) 

Even though it looks the same as "qrcode.png" a quick comparision of the two would show otherwise
![qrcode](./assets/absolute_error.png?raw=true) 

## Finally scanning "the merged_img.png" seems to work too
![qrcode](./assets/merged_img_qr_scan.png?raw=true) 

## To decode the hidden text back run the following script
```bash
python reconstruct.py
```

This will print the hidden text from the hidden image
