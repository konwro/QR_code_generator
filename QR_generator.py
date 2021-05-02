# Task: Generate custom QR code
# pip install qrcode

# Step 0: import
import qrcode
import qrcode.image.svg

# Step 1: initate customize QR code
qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 25,
    border = 1)

# Step 2: specify data
data_to_qr = 'Hello 666 !!!'
    
qr.add_data(data_to_qr)
qr.make(fit=True)

# Step 3: Option fo vector-graphic
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make(data_to_qr, image_factory = factory)

# Step 4:

# Step 5: generate output
img = qr.make_image(fill_color='black', back_color='white')
img.save('generatedQR.png')
svg_img.save('generatedQR.svg')