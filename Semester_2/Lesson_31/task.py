import os
import sys


from PIL import Image, ImageDraw, ImageFont


def txt_on_pics(file_read, file_write):
    pics = os.listdir(file_read)

    for pic in pics:
        pic_format = pic[pic.index(".") + 1 :]
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
            fnt = ImageFont.truetype(
                "/usr/share/fonts/truetype/freefont/lato/Lato-Regular.ttf", 28
            )
            position = (img.height - 180, img.width - 30)
            txt_color = (200, 10, 40)
            draw.text(position, txt, fill=txt_color, font=fnt)

            if pic_format == "png":
                format = "jpg"
            elif pic_format in ("jpg", "jpeg"):
                format = "png"

            pic_abs = pic[: pic.index(".")]
            pic_save_path = os.path.join(file_write, f"{pic_abs}.{format}")

            img.save(pic_save_path, format)

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
