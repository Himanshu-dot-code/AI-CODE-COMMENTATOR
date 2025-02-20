import qrcode

# URL of your project repository or document
project_url = "https://github.com/Himanshu-dot-code/AI-CODE-COMMENTATOR.git"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(project_url)
qr.make(fit=True)

# Create and save the QR Code image
qr_img = qr.make_image(fill="black", back_color="white")
qr_img.save("project_qr.png")

print("QR Code generated successfully! Check 'project_qr.png'.")
