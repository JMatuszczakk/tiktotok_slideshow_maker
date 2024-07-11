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
    