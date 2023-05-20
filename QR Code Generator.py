# QR Code Generator made by HitMonkey69



import qrcode
import pyfiglet

banner = pyfiglet.figlet_format('Welcome to QR Code Generator')
print(banner)
print('Enter 1 to generate QR Code')
print('Enter 2 to Quit')

while True:
    usr = int(input('Enter your choice here:'))

    if usr == 1:

        qr = qrcode.QRCode(
            version = 15,
            box_size = 10,
            border = 5
        )

        data = input('Enter your link here:')
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        img.save('text.png')
        
        banner2 = pyfiglet.figlet_format('QR Code generated successfully')
        print(banner2)

        print('To generate more enter 1')
        print('To quit enter 2')

    elif usr == 2:
        banner3 = pyfiglet.figlet_format('Have a nice day')
        print(banner3)
        break
        

    else :
        print('Wrong input try again.')