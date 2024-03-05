# QRGen
## Features

- **URL to QR Code Conversion**: Easily convert URLs into QR codes with a simple function call.
- **Minimalist Design**: The generator prioritizes simplicity and efficiency, ensuring a streamlined user experience.
- **High-Quality QR Codes**: Generate high-resolution QR codes suitable for printing or digital use.
- **Customization Options**: Customize QR code size, color, and error correction level to meet specific requirements.
- **Cross-Platform Compatibility**: Compatible with Windows, macOS, and Linux operating systems.

## Installation

1. Clone the repository to your local machine:

 ```powershell
git clone https://github.com/your-username/qr-code-generator.git
```

2. Install the required dependencies:

 ```powershell
pip install -r requirements.txt
```

3. Run the generator:

 ```powershell
python qr_generator.py
```

## Usage

1. Import the `generate_qr_code` function from `qr_generator.py`.
2. Call the function with the URL you want to convert to a QR code.
3. Customize optional parameters if needed.
4. The function will generate the QR code image and save it to the specified location.

```python
from qr_generator import generate_qr_code

# Example usage
url = "https://example.com"
output_file = "qr_code.png"

generate_qr_code(url, output_file)
```

