import qrcode
from PIL import Image
import qrcode.constants

link=input("Enter Your Link : ")
qr=qrcode.QRCode(version=1.0,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data(link)
qr.make(fit=True)
img=qr.make_image(fill_color="#A31D1D",back_color="#E5D0AC")
img.save("qr.png")