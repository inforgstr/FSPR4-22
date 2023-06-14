import os
import sys


from PIL import Image, ImageDraw, ImageFont


def txt_on_pics(file_read, file_write):
    try:
        pics = os.listdir(file_read)
    except FileNotFoundError as error:
        return error
    
    font_path = "/usr/share/fonts/truetype/freefont/lato/Lato-Regular.ttf"
    font_size = 30
    txt_color = (255, 0, 0)

    for pic in pics:
        pic_format = pic[pic.index(".") + 1 :].lower()

        if pic_format in ("jpeg", "jpg", "png"):
            pic_path = os.path.join(file_read, pic)

            try:
                with Image.open(pic_path) as img:
                    img.load()

            except FileNotFoundError as error:
                return error

            os.makedirs(file_write, exist_ok=True)

            # Drawing Hello, World! into picture
            draw = ImageDraw.Draw(img)
            txt = "Hello, World!"
            fnt = ImageFont.truetype(font_path, font_size)
            position = (img.width - 180, img.height - 30)
            txt_color = (200, 10, 40)
            draw.text(position, txt, fill=txt_color, font=fnt)

            if pic_format == "png":
                output_format = "jpg"
            elif pic_format in ("jpg", "jpeg"):
                output_format = "png"

            pic_abs = os.path.splitext(pic)[0]
            pic_save_path = os.path.join(file_write, f"{pic_abs}.{output_format}")

            img.save(pic_save_path, output_format)

    return "Success"


try:
    file_read = sys.argv[1]

    if file_read != "--help":
        file_write = sys.argv[2]

        print(txt_on_pics(file_read, file_write))
    else:
        print("\nCommands:\n\tpython [FILE NAME] [FILE TO READ] [FILE TO WRITE]\n")

except (NameError, IndexError) as error:
    print(error)
