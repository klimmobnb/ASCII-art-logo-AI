from PIL import Image
import pytesseract

def convert_image_to_ascii(image_path, width=100):
    # Load the image
    image = Image.open(image_path)
    # Resize the image
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio / 2)
    resized_image = image.resize((width, new_height))
    # Convert image to grayscale
    grayscale_image = resized_image.convert('L')
    # Perform OCR to extract text from the image
    text = pytesseract.image_to_string(grayscale_image)
    return text

def generate_ascii_logo(text):
    # Convert text to ASCII art
    ascii_logo = ""
    for char in text:
        ascii_char = char if char.isalnum() or char.isspace() else ' '
        ascii_logo += ascii_char
    return ascii_logo

def main():
    # Path to the image file
    image_path = "logo_image.png"
    # Convert image to ASCII art
    ascii_text = convert_image_to_ascii(image_path)
    # Generate ASCII logo
    ascii_logo = generate_ascii_logo(ascii_text)
    # Print the ASCII logo
    print(ascii_logo)

if __name__ == "__main__":
    main()
