from PIL import Image

def create_particles(image: Image, width: int, height: int):
    output = ""
    current_pixel = 0
    pixels = list(image.getdata())
    imagesize = image.size
    for y in range(imagesize[1]):
        for x in range(imagesize[0]):
            current_colors = (pixels[current_pixel][0] / 255, pixels[current_pixel][1] / 255, pixels[current_pixel][2] / 255)
            output += f"particle minecraft:dust {current_colors[0]} {current_colors[1]} {current_colors[2]} 0.5 ^{x * width / imagesize[0]} ^{(imagesize[1] -  y) * height / imagesize[1] + 2} ^\n"
            current_pixel += 1
    return output

if __name__ == "__main__":
    import argparse
    argumentparser = argparse.ArgumentParser()
    argumentparser.add_argument("file")
    argumentparser.add_argument("width")
    argumentparser.add_argument("height")
    argumentparser.add_argument("output")
    args = argumentparser.parse_args()

    with open(args.output, "w") as outputfile:
        outputfile.write(create_particles(Image.open(args.file), int(args.width), int(args.height)))