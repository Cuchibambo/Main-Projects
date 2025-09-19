import qrcode
import os

qr = qrcode.QRCode(
    version=1, # 1 to 40, controls the size of the QR Code
    # error_correction=qrcode.constants.ERROR_CORRECT_L, # <= 7% errors corrected
    error_correction=qrcode.constants.ERROR_CORRECT_M, # <= 15% errors corrected
    # error_correction=qrcode.constants.ERROR_CORRECT_Q, # <= 25% errors corrected
    # error_correction=qrcode.constants.ERROR_CORRECT_H, # <= 30% errors corrected
    box_size=10, # px per px of qrcode
    border=4, # qrcode pxs border size
)

name = "qrcode_M.png"
# qr.add_data('https://youtube.com') # Basic format, e.g. link or plain text
qr.add_data('tel:0033768332252') # tel:[Phone Number]
# qr.add_data('smsto:0033768332252:Yo Maurice tu est vrmt trop beau') # smsto:[Phone Number]:[Message]
# qr.add_data('mailto:m.aubin.iribarren@gmail.com?subject=SUBJECT&body=BODY') # mailto:[Email Address]?subject=[Subject]&body=[Body]
# qr.add_data('geo:48.8588443,2.2943506') # geo:[Latitude],[Longitude]
# qr.add_data('WIFI:S:Freebox-364278;T:WPA;P:tr2b5qx643qzn5tzqnk6m2;;') # WIFI:S:[SSID];T:[WEP|WPA];P:[Password];;
# qr.add_data('BEGIN:VCARD\nVERSION:3.0\nN:Last-name;First-name\nORG:CompanyName\nTITLE:JobTitle\nADR:;;123 Sesame St;SomeCity;CA;12345;USA\nTEL;WORK;VOICE:1234567890\nTEL;CELL:Mobile\nEMAIL;WORK;INTERNET:foo@email.com\nURL:http://website.com\nEND:VCARD')
qr.make(fit=True)
save_path = os.path.join(r"c:\Users\maubi\Bureau\Programation\python\QrCodes", name)
img = qr.make_image(fill_color="#67636B", back_color="#1F1F1F")
img.save(save_path)

# dbc951b4ab01646888b2a91da73a94dd920054c2f27c8cfeacae3eba298e71b0
# ff16579d09927da6bd84b42261aa8e7095f89399d5f633011f0ae039b4e2ed8b