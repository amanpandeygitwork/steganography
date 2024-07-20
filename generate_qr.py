import segno

#generating a qr code
msg = input()
qrcode = segno.make_qr(msg)
qrcode.save("qrcode.png",scale=8)
