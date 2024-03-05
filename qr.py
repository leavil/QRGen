import qrcode


def generate_qr_code(url, file_name):
    # Create a QRCode object
    qr_code = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add the URL to the QR code
    qr_code.add_data(url)
    qr_code.make(fit=True)

    # Create an image of the QR code
    qr_image = qr_code.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_image.save(file_name)

if __name__ == "__main__":
    url = input("Enter the web address: ")
    file_name = input("Enter the image file name: ")
    generate_qr_code(url, file_name)
    print("QR code generated successfully.")
