import sys
from PIL import Image, ImageOps

while True:
    if len(sys.argv) == 3:
        a = str(sys.argv[1]).lower()
        a1, a2 = a.split(".")

        b = str(sys.argv[2]).lower()
        b1, b2 = b.split(".")

        if a2 not in ["jpeg", "jpg", "png"]:
            sys.exit("Invalid input")
        elif b2 not in ["jpeg", "jpg", "png"]:
            sys.exit("Invalid output")
        elif a2 != b2:
            sys.exit("Input and output have different extensions")
        else:
            break
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")


try:
    h_shirt = Image.open("shirt.png")
    h_size = h_shirt.size

    muppet_pic = Image.open(sys.argv[1])
    muppet_pic = ImageOps.fit(muppet_pic, h_size, method=Image.BICUBIC, bleed=0.0, centering=(0.5,0.5))
    muppet_pic.paste(h_shirt, h_shirt)
    muppet_pic.save(sys.argv[2])

except (FileNotFoundError, AttributeError):
    sys.exit("File does not exist")


