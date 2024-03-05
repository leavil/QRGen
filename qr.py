import qrcode


def generar_codigo_qr(url, nombre_archivo):
    # Crea un objeto QRCode
    codigo_qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Añade la URL al código QR
    codigo_qr.add_data(url)
    codigo_qr.make(fit=True)

    # Crea una imagen del código QR
    imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

    # Guarda la imagen del código QR
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    url = input("Introduce la dirección web: ")
    nombre_archivo = input("Introduce el nombre del archivo de imagen: ")
    generar_codigo_qr(url, nombre_archivo)
    print("Se ha generado el código QR correctamente.")