import qrcode#import

link = input("Please enter a website link: ")#user inputs website link that qrcode directs to when used

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)#parameters set for design of qrcode
qr.add_data(link)
qr.make()

img = qr.make_image(fill_color = black, back_color = white)#parameters set for colors of qrcode
img.save('')#insert link chosen earlier