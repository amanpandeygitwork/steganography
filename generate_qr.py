import qrcode

#generating a qr code
msg = input()
qr = qrcode.make(msg)
qr.save("qrcode.png")
