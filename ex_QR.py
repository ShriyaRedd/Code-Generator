


# Import necessary libraries
import qrcode  # For generating QR codes
from PIL import Image  # For image manipulation and saving the QR code as an image

# Function to generate a QR code
def generate_qr_code(data, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=10, border=4, fill_color="black", back_color="white", filename="qr_code.png"):
    """
    Generates a QR code and saves it as an image file.

    :param data: The data to encode into the QR code (string)
    :param version: The size of the QR code matrix (default: 1)
    :param error_correction: Error correction level (default: ERROR_CORRECT_L)
    :param box_size: The size of each box in the QR code (default: 10)
    :param border: The thickness of the border (default: 4)
    :param fill_color: The color of the QR code (default: black)
    :param back_color: The background color of the QR code (default: white)
    :param filename: The filename to save the image as (default: qr_code.png)
    """
    # Create a QR code instance with the specified parameters
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image as a PNG file
    img.save(filename)
    print(f"QR code generated and saved as '{filename}'.")

# Main function to handle user input and call the QR code generator
def main():
    # Get data to encode into the QR code from the user
    data = input("Enter the data to encode in the QR code: ")

    # Optional customization
    customize = input("Do you want to customize the QR code (yes/no)? ").lower()
    if customize == 'yes':
        try:
            # Get user inputs for customization
            version = int(input("Enter the QR code version (1 to 40, 1 is the smallest): "))
            error_correction = input("Enter the error correction level (L, M, Q, H): ").upper()
            box_size = int(input("Enter the box size (default is 10): "))
            border = int(input("Enter the border size (default is 4): "))
            fill_color = input("Enter the QR code color (default is black): ")
            back_color = input("Enter the background color (default is white): ")
            filename = input("Enter the filename to save as (e.g., 'my_qr_code.png'): ")

            # Map error correction level to qrcode constants
            error_correction_mapping = {
                'L': qrcode.constants.ERROR_CORRECT_L,
                'M': qrcode.constants.ERROR_CORRECT_M,
                'Q': qrcode.constants.ERROR_CORRECT_Q,
                'H': qrcode.constants.ERROR_CORRECT_H
            }

            # Generate the QR code with the custom settings
            generate_qr_code(
                data=data,
                version=version,
                error_correction=error_correction_mapping.get(error_correction, qrcode.constants.ERROR_CORRECT_L),
                box_size=box_size,
                border=border,
                fill_color=fill_color,
                back_color=back_color,
                filename=filename
            )

        except ValueError as e:
            print(f"Invalid input, using default values. Error: {e}")
            # If the user input is invalid, generate the QR code with default settings
            generate_qr_code(data)
    else:
        # Generate the QR code with default settings
        generate_qr_code(data)

# Run the main function
if __name__ == "__main__":
    main()

