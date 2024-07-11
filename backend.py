from PIL import Image, ImageDraw, ImageFont

def add_centered_text_to_image(image_path, text, font_size, output_path):
    # Open the existing image
    font_path = "ttf.ttf"  # Replace with your font file path

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    def wrap_text(text, font, max_width):
            lines = []
            words = text.split()
            while words:
                line = ''
                while words and draw.textbbox((0, 0), line + words[0], font=font)[2] <= max_width:
                    line = line + (words.pop(0) + ' ')
                lines.append(line.strip())
            return lines
        # Get image dimensions
    image_width, image_height = image.size

    # Wrap the text
    wrapped_text = wrap_text(text, font, image_width - 20)  # 20 pixels padding

    # Calculate total text height
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in wrapped_text)

    # Calculate starting y position
    y_start = (image_height - total_text_height) // 2

    # Draw each line of text
    current_y = y_start
    for line in wrapped_text:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        text_height = draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1]
        x = (image_width - text_width) // 2
        draw.text((x, current_y), line, fill='white', font=font)
        current_y += text_height

    # Save the image
    image.save(output_path)
    return image
if __name__ == "__main__":
    # Usage example
    image_path = "2.jpeg"  # Replace with the path to your image
    text = "This is a sample text that will be wrapped and centered on the image."
    font_path = "ttf.ttf"  # Replace with your font file path
    font_size = 30
    output_path = "output_image3.png"

    add_centered_text_to_image(image_path, text, font_path, font_size, output_path)
