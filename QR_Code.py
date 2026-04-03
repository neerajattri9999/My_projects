# import qrcode as qr #alias name qr
# img=qr.make("https://www.linkedin.com/in/neeraj-attri-63b250196/")
# img.save("MyProfile.png")

# import qrcode as qr #alias name qr
# from PIL import Image
# qr=qr.QRCode(Version=1, 
#              error_correction=qr.constants.ERROR_CORRECT_H,
#              box_size=10, border=4)
# qr.add_data("hi how are you ?")


################


import qrcode

qr = qrcode.QRCode(
    version=1,  # ✅ lowercase 'version'
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("hi how are you?")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
